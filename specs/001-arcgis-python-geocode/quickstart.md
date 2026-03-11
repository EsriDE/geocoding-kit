# Quickstart: ArcGIS Geocoding Example (Python)

This quickstart shows how to run the example script that geocodes a list of addresses from a CSV file using ArcGIS Location Platform.

## 1) Clone the repository

```bash
git clone <repo-url>  # replace with your repo URL
cd geocoding-kit
```

## 2) Create a Python virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## 3) Install dependencies

```bash
pip install -r requirements.txt
```

## 4) Set your ArcGIS API key

The example expects an environment variable named `ARCGIS_API_KEY`. You can set it in your shell:

```bash
export ARCGIS_API_KEY="<your-api-key>"
```

Alternatively, create a `.env` file in the repo root with:

```
ARCGIS_API_KEY=<your-api-key>
```

## 5) Run the example

Prepare a CSV file with at least one column named `address`.

Example input (`addresses.csv`):

```csv
address
380 New York St, Redlands, CA 92373
1600 Pennsylvania Ave NW, Washington, DC 20500
invalid address example
```

Run the script:

```bash
python examples/geocode_addresses.py --input addresses.csv --output results.csv
```

## 6) Inspect the output

The output CSV (`results.csv`) includes the original address and one row per input with columns like:

- `matched_address`
- `latitude`
- `longitude`
- `score`
- `match_status`
- `error` (if any)

## 7) Troubleshooting

- If you see an authentication failure, verify `ARCGIS_API_KEY` is set correctly.
- If you hit rate limiting (HTTP 429), retry after waiting or reduce batch size.
