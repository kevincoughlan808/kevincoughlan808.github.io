from __future__ import annotations

import logging
import sys
from typing import Any

import requests

COINDESK_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
REQUEST_TIMEOUT_SECONDS = 10


def fetch_current_price(url: str = COINDESK_URL) -> dict[str, Any]:
    response = requests.get(url, timeout=REQUEST_TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    try:
        payload = fetch_current_price()
    except requests.RequestException as exc:
        logging.exception("Failed to fetch current price data.")
        return 1

    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
