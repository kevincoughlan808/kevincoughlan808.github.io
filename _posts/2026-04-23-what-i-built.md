---
layout: post
title: "What I built"
date: 2026-04-23
---

Short week for side project stuff, but I got one of the bigger items off my list.

## What I built

Added the `/history` endpoint. It logs each price fetch to a local SQLite database with a timestamp, and the endpoint returns the last 24 hours of entries as JSON. Used `aiosqlite` to keep things async and avoid blocking the main event loop. The table schema is dead simple — just `id`, `price`, and `timestamp`.

I also finally wrote up the deployment notes in the README. Nothing detailed, just the Railway setup steps and the environment variables needed. Future me will thank present me.

## What I learned

- SQLite on Railway works fine but the storage is ephemeral. If the instance restarts, the history resets. Not a dealbreaker for now since I'm mostly just experimenting, but it means I'll need to think about persistent storage eventually.
- I wasted a good chunk of one evening trying to get the database to initialize cleanly on startup. Ended up being a path issue — I was writing to a relative path that didn't exist in the Railway environment. Hardcoding `/tmp/` as the db location fixed it. Not pretty, but it works.
- Writing docs while the setup is still fresh is so much easier than doing it weeks later. Obvious advice that I keep ignoring.

## Next up

- Look into Railway's volume storage or just switch to a free Postgres tier so history actually persists.
- Start on that simple front end — thinking a single HTML page with a chart using Chart.js or something lightweight.

---
*This post was written by my weekly Claude blog agent.*

---
*This post was written by my weekly Claude blog agent.*
