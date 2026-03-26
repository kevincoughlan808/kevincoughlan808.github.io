from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Iterable

import requests
from fastapi import FastAPI, HTTPException

REQUEST_TIMEOUT_SECONDS = 10


@dataclass(frozen=True)
class PricePoint:
    timestamp_utc: str
    currency: str
    price: float


@dataclass(frozen=True)
class Provider:
    name: str
    url: str
    parser: Callable[[dict[str, Any]], PricePoint]


def _iso_from_epoch(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(epoch_seconds, tz=timezone.utc).isoformat()


def _parse_coindesk(payload: dict[str, Any]) -> PricePoint:
    updated_iso = payload["time"]["updatedISO"]
    rate_float = float(payload["bpi"]["USD"]["rate_float"])
    return PricePoint(timestamp_utc=updated_iso, currency="USD", price=rate_float)


def _parse_coingecko(payload: dict[str, Any]) -> PricePoint:
    data = payload["bitcoin"]
    rate_float = float(data["usd"])
    updated_iso = _iso_from_epoch(float(data["last_updated_at"]))
    return PricePoint(timestamp_utc=updated_iso, currency="USD", price=rate_float)


def _parse_coinbase(payload: dict[str, Any]) -> PricePoint:
    data = payload["data"]
    rate_float = float(data["amount"])
    updated_iso = datetime.now(tz=timezone.utc).isoformat()
    return PricePoint(timestamp_utc=updated_iso, currency=data["currency"], price=rate_float)


PROVIDERS: tuple[Provider, ...] = (
    Provider(
        name="coindesk",
        url="https://api.coindesk.com/v1/bpi/currentprice.json",
        parser=_parse_coindesk,
    ),
    Provider(
        name="coingecko",
        url=(
            "https://api.coingecko.com/api/v3/simple/price"
            "?ids=bitcoin&vs_currencies=usd&include_last_updated_at=true"
        ),
        parser=_parse_coingecko,
    ),
    Provider(
        name="coinbase",
        url="https://api.coinbase.com/v2/prices/spot?currency=USD",
        parser=_parse_coinbase,
    ),
)


def fetch_current_btc_price(providers: Iterable[Provider] = PROVIDERS) -> PricePoint:
    last_error: Exception | None = None
    for provider in providers:
        try:
            response = requests.get(provider.url, timeout=REQUEST_TIMEOUT_SECONDS)
            response.raise_for_status()
            payload: dict[str, Any] = response.json()
            return provider.parser(payload)
        except (requests.RequestException, KeyError, ValueError, TypeError) as exc:
            logging.warning("Provider %s failed: %s", provider.name, exc)
            last_error = exc

    raise RuntimeError("All providers failed.") from last_error


app = FastAPI()


@app.get("/price")
def get_price() -> dict[str, Any]:
    try:
        point = fetch_current_btc_price(PROVIDERS)
    except RuntimeError as exc:
        raise HTTPException(
            status_code=503,
            detail="All providers failed. Check your internet/DNS settings.",
        ) from exc

    return {
        "timestamp_utc": point.timestamp_utc,
        "currency": point.currency,
        "price": round(point.price, 2),
    }
