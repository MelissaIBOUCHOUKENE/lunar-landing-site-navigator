# Lunar Landing Site Navigator

Project for the **2026 NASA Space Apps Challenge** — "Lunar Landing Site Navigator".

A web tool to quickly compare two lunar landing sites: **Sun** and **Earth** positions relative to the horizon, **solar power** potential and **direct-to-Earth communication** windows over 30 days.

**Live demo:** https://lunar-site-navigator.github.io/lunar-landing-site-navigator/

## Features
- Side-by-side comparison of two sites (17 sites: Apollo, Chang'e, Chandrayaan-3, SLIM, south pole / Artemis candidates...).
- Date picker with quick shifts (−1, +1, +3, +7 days) to simulate a landing delay.
- Sky view (Sun and Earth vs. horizon) and 30-day elevation curves.
- Simple verdicts: solar power (good / medium / poor) and communications (continuous / in windows / very limited).
- Time remaining before the next Sun and Earth set or rise.
- Custom site (latitude / longitude) using a simplified model, **indicative only**.

## Data
Sun and Earth positions come from the **JPL Horizons System**, queried by `fetch_horizons.py` (2-hour steps, 120 days from 2026-11-15) and stored in `data.json`.

Regenerate the data:
```
python fetch_horizons.py 2026-11-15 120
```

## Files
- `index.html`: the application (single page, no dependencies)
- `data.json`: precomputed data
- `fetch_horizons.py`: script that downloads the data

## Limitations
- The horizon is assumed **flat**: real terrain (LOLA data) is not used, so permanently shadowed crater floors are not represented correctly.
- Site coordinates are rounded.
- Outside the dates covered by `data.json`, and for custom sites, the app falls back to a simplified, approximate model.

## Future work
Use LOLA terrain for a real horizon profile, add more sites, compute ephemerides for arbitrary coordinates.

## Sources and credits
- [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) (NASA/JPL)
- [Quickmap](https://quickmap.lroc.asu.edu/) (ASU / LROC) and [Moon Trek](https://trek.nasa.gov/moon/) (NASA) for terrain exploration
- [Canadian Space Agency](https://www.asc-csa.gc.ca/eng/astronomy/moon-exploration/)

This is an independent project: it is not endorsed or approved by NASA, which is not responsible for its content. Data remain subject to each source's terms of use.
