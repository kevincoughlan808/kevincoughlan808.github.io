---
layout: post
title: "What I built"
date: 2026-04-15
---

Since the last update I've been chipping away at the crypto API. Mostly focused on the caching piece I mentioned and getting the thing actually running somewhere other than my laptop.

## What I built

Added basic in-memory caching to the `/price` endpoint using `cachetools`. It holds the last fetched price for 60 seconds before hitting the providers again. Nothing fancy, but it cuts down on redundant calls and makes the response times way more consistent.

I also got the app deployed on Railway. First time using it — the setup was surprisingly painless. Connected the GitHub repo, set a couple of environment variables, and it was live. Took maybe 20 minutes total including the time I spent reading their docs.

## What I learned

- Caching even at a basic level makes a noticeable difference. I was hammering the provider APIs way more than I needed to.
- Railway's free tier has limits I'll need to keep an eye on, but for a side project it's more than enough right now.
- I spent too long debating between Redis and in-memory caching. For a single-instance app with one user (me), `cachetools` was the obvious choice. I just needed to stop overthinking it.

## Next up

- Add a `/history` endpoint that stores prices over time in a simple SQLite database.
- Write up some basic deployment notes in the repo README so I don't forget how I set things up.
- Maybe look into a simple front end to display the price — even just a single-page HTML thing.

---
*This post was written by my weekly Claude blog agent.*
