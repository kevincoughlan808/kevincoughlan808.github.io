---
layout: post
title: "Progress Update: Crypto Price API and Repo Cleanup"
date: 2026-04-01
---

Since the last post, I’ve built a small Bitcoin price API and cleaned up my project structure.

## What I built

I created a simple FastAPI app that exposes a `/price` endpoint to fetch the latest BTC price on demand, plus a `/health` endpoint for a quick uptime check. It pulls from multiple public providers and returns JSON.

## Project setup wins

- Split the crypto app into its own GitHub repo for clarity.
- Moved my blog into its own dedicated folder so the Jekyll site is isolated.
- Tidied up the workspace so each project lives in its own top‑level directory.

Next up: improve the API with caching and add some deployment notes.
