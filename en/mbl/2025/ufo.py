import pandas as pd
import numpy as np
import zipfile
import pymc as pm
import arviz as az
from math import radians, sin, cos, sqrt, atan2
import re

def ufo_sighting_nuke_counts():
    nuke_path = "../../2023/01/nuke.csv"
    nukes = pd.read_csv(nuke_path)

    nuke_coords = nukes[["latitude", "longitude"]].astype(float).to_numpy()

    ufo_zip_path = "/opt/Downloads/ufo/ufo.csv.zip"
    with zipfile.ZipFile(ufo_zip_path, 'r') as z:
        with z.open("ufo.csv") as f:
            ufo = pd.read_csv(f)

    cities_path = "/opt/Downloads/ufo/us-cities.csv"
    cities = pd.read_csv(cities_path)

    def normalize_city_name(name):
        if not isinstance(name, str):
            return None
        name = name.lower().strip()
        suffixes = [
            " city", " town", " village", " municipality",
            " borough", " township", " cdp", " city and borough"
        ]
        for s in suffixes:
            if name.endswith(s):
                name = name[:-len(s)]
        return name.strip()

    cities["city_norm"] = cities["city"].map(normalize_city_name)
    cities["state_norm"] = cities["state"].str.strip().str.upper()

    def parse_city_state(loc):
        if not isinstance(loc, str):
            return None, None
        loc = loc.strip()

        # Pattern: "City, ST"
        m = re.match(r"^(.*?),\s*([A-Za-z]{2})$", loc)
        if m:
            return m.group(1).strip().lower(), m.group(2).upper()

        # Pattern: "City ST"
        m = re.match(r"^(.*?)\s+([A-Za-z]{2})$", loc)
        if m:
            return m.group(1).strip().lower(), m.group(2).upper()

        return None, None

    ufo["city_norm"], ufo["state_norm"] = zip(*ufo["Location"].map(parse_city_state))
    ufo["city_norm"] = ufo["city_norm"].map(normalize_city_name)

    ufo = ufo.merge(
        cities[["city_norm", "state_norm", "latitude", "longitude"]],
        on=["city_norm", "state_norm"],
        how="left"
    )

    #print("Total UFO rows:", len(ufo))
    #print("Geocoded UFO rows:", ufo[["latitude", "longitude"]].notna().all(axis=1).sum())
    #rint("Missing geocode rows:", ufo[["latitude", "longitude"]].isna().any(axis=1).sum())

    def parse_year(x):
        if not isinstance(x, str):
            return None

        # UFO format typically is YYYYMMDD
        m = re.match(r"^(\d{4})", x)
        if m:
            year = int(m.group(1))
            if 1900 < year < 2100:
                return year
        return None

    ufo["year"] = ufo["DateOccurred"].map(parse_year)
    ufo = ufo.dropna(subset=["year"])
    ufo["year"] = ufo["year"].astype(int)

    def haversine(lat1, lon1, lat2, lon2):
        R = 6371.0
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
        return 2 * R * atan2(sqrt(a), sqrt(1-a))

    ufo["near_nuke"] = False

    for idx, row in ufo.iterrows():
        lat, lon = row["latitude"], row["longitude"]
        if pd.isna(lat) or pd.isna(lon):
            continue
        for lat2, lon2 in nuke_coords:
            if haversine(lat, lon, lat2, lon2) <= 100:
                ufo.at[idx, "near_nuke"] = True
                break

    near = ufo[ufo["near_nuke"]]
    far  = ufo[~ufo["near_nuke"]]

    near_counts = near.groupby("year").size().sort_index()
    far_counts  = far.groupby("year").size().sort_index()

    years = sorted(set(near_counts.index).union(far_counts.index))

    near_array = np.array([near_counts.get(y, 0) for y in years])
    far_array  = np.array([far_counts.get(y, 0) for y in years])

    np.random.seed(1)

    scale_factor = near_array.sum() / far_array.sum()
    far_scaled = np.round(far_array * scale_factor).astype(int)

    #print("Years:", years[-10:])
    #print("UFOs near nuclear sites:", near_array[-10:])
    #print("UFOs elsewhere (scaled):", far_scaled[-10:])

    years = np.array(years)               # e.g. [1901, 1910, ...]
    near = np.array(near_array)
    far  = np.array(far_scaled)
    return years, near, far

def poisson_ratio(years, near, far):

    n_years = len(years)
    counts = np.concatenate([near, far])
    group = np.concatenate([np.ones(n_years, dtype=int), np.zeros(n_years, dtype=int)])  # 1 near, 0 far
    year_idx = np.concatenate([np.arange(n_years), np.arange(n_years)])  # index into year effects
    N = counts.size

    with pm.Model() as model:
        sigma_year = pm.HalfNormal("sigma_year", sigma=1.0)      # reasonable default, tweak if needed

        year_offset = pm.Normal("year_offset", mu=0.0, sigma=1.0, shape=n_years)
        year_effect = pm.Deterministic("year_effect", year_offset * sigma_year)

        alpha = pm.Normal("alpha", mu=0.0, sigma=2.0)   # base log-rate
        beta  = pm.Normal("beta", mu=0.0, sigma=1.0)    # log rate difference (near - far)
        log_mu = alpha + beta * group + year_effect[year_idx]

        mu = pm.Deterministic("mu", pm.math.exp(log_mu))
        obs = pm.Poisson("obs", mu=mu, observed=counts)

        rate_ratio = pm.Deterministic("rate_ratio", pm.math.exp(beta))

        trace = pm.sample(draws=2000, tune=1500, target_accept=0.95, return_inferencedata=True)

    print(az.summary(trace, var_names=["alpha", "beta", "sigma_year", "rate_ratio"], round_to=3))

    rr_samples = trace.posterior["rate_ratio"].values.flatten()
    p_gt_1 = (rr_samples > 1).mean()
    print(f"P(rate_ratio > 1) = {p_gt_1:.3f}")

    rr_samples = trace.posterior["rate_ratio"].values.flatten()

    print("Median rate ratio:", np.median(rr_samples))
    print("Mean rate ratio:", np.mean(rr_samples))
    print("95% HDI:", az.hdi(rr_samples, hdi_prob=0.95))
    print("P(rate_ratio > 1):", (rr_samples > 1).mean())
    print("P(0.9 <= rr <= 1.1):", ((rr_samples >= 0.9) & (rr_samples <= 1.1)).mean())
    
