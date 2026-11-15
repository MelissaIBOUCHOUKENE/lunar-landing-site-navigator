#!/usr/bin/env python3
"""Récupère azimut/élévation du Soleil et de la Terre (vus depuis chaque site lunaire)
via l'API JPL Horizons et écrit data.json.

Usage : python fetch_horizons.py [DATE_DEBUT=2026-11-15] [NB_JOURS=120]
Puis, dans l'appli, bouton « Charger data.json ».
"""
import json, sys, time, urllib.parse, urllib.request
from datetime import datetime, timedelta

# Mêmes noms que dans l'appli (lat°, lon° Est)
SITES = {
    "Apollo 11": (0.67, 23.47),
    "Apollo 17": (20.19, 30.77),
    "Chandrayaan-3": (-69.37, 32.32),
    "Malapert (massif)": (-85.99, 0.12),
    "Shackleton (rebord)": (-89.9, 0.0),
    "Nobile (Artemis)": (-85.4, 31.4),
    "Connecting Ridge (Artemis III)": (-89.45, -137.3),
    "Mons Mouton (IM-2)": (-84.8, 29.2),
    "Apollo 12": (-3.01, -23.42),
    "Apollo 14": (-3.65, -17.47),
    "Apollo 15": (26.13, 3.63),
    "Apollo 16": (-8.97, 15.50),
    "Chang'e 3": (44.12, -19.51),
    "Chang'e 4": (-45.46, 177.59),
    "Chang'e 5": (43.06, -51.92),
    "Chang'e 6": (-41.64, -153.99),
    "SLIM": (-13.32, 25.25),
}
START = sys.argv[1] if len(sys.argv) > 1 else "2026-11-15"
DAYS = int(sys.argv[2]) if len(sys.argv) > 2 else 120
STEP_H = 2
API = "https://ssd.jpl.nasa.gov/api/horizons.api"


def fetch(body, lat, lon, start, stop):
    q = {
        "format": "json", "COMMAND": f"'{body}'", "OBJ_DATA": "'NO'",
        "MAKE_EPHEM": "'YES'", "EPHEM_TYPE": "'OBSERVER'",
        "CENTER": "'coord@301'", "COORD_TYPE": "'GEODETIC'",
        "SITE_COORD": f"'{lon % 360},{lat},0'",
        "START_TIME": f"'{start}'", "STOP_TIME": f"'{stop}'",
        "STEP_SIZE": f"'{STEP_H * 60}m'", "QUANTITIES": "'4'",
        "ANG_FORMAT": "'DEG'", "CSV_FORMAT": "'YES'",
    }
    url = API + "?" + urllib.parse.urlencode(q)
    with urllib.request.urlopen(url, timeout=60) as r:
        res = json.load(r)
    txt = res.get("result", "")
    if "$$SOE" not in txt:
        raise RuntimeError(txt[:500])
    rows = txt.split("$$SOE")[1].split("$$EOE")[0].strip().splitlines()
    out = []
    for line in rows:
        f = [x.strip() for x in line.split(",")]
        out.append([round(float(f[3]), 2), round(float(f[4]), 2)])  # [az, el]
    return out


def main():
    t0 = datetime.fromisoformat(START)
    t1 = t0 + timedelta(days=DAYS)
    data = {"start": t0.strftime("%Y-%m-%dT%H:%M:%SZ"), "step_h": STEP_H, "sites": {}}
    for name, (lat, lon) in SITES.items():
        print("→", name, flush=True)
        s = fetch("10", lat, lon, t0.strftime("%Y-%m-%d %H:%M"), t1.strftime("%Y-%m-%d %H:%M"))
        e = fetch("399", lat, lon, t0.strftime("%Y-%m-%d %H:%M"), t1.strftime("%Y-%m-%d %H:%M"))
        data["sites"][name] = {"lat": lat, "lon": lon, "sun": s, "earth": e}
        time.sleep(1)  # politesse envers l'API
    with open("data.json", "w") as fh:
        json.dump(data, fh)
    print("OK : data.json écrit")


if __name__ == "__main__":
    main()
