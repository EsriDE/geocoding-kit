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

Prepare a CSV file with the following required columns: `id`, `address`, `postal`, `city`, `country`.

Example input (`addresses.csv`):

```csv
id,address,postal,city,country
1,Karl-Liebknecht-Straße 5,10178,Berlin,DE
2,Adenauerallee 206,53113,Bonn,DE
3,Wendenstraße 8 - 12,20097,Hamburg,DE
4,Freundallee 23,30173,Hannover,DE
5,Konrad-Adenauer-Ufer 41-45,50668,Köln,DE
6,Ringstraße 7,85402,Kranzberg,DE
7,Fechnerstraße 8,04155,Leipzig,DE
8,Martin-Luther-King-Weg 24,48155,Münster,DE
```

Run the script:

```bash
python examples/geocode_addresses.py --input addresses.csv --output results.csv
```

You can also pass a key directly (overrides `ARCGIS_API_KEY`):

```bash
python examples/geocode_addresses.py --input addresses.csv --output results.csv --key "$ARCGIS_API_KEY"
```

## 6) Inspect the output

The output CSV (`results.csv`) includes the original address and one row per input with columns like:

- `id`
- `matched_address`
- `latitude`
- `longitude`
- `score`
- `match_type`
- `match_status`

## 7) Troubleshooting

- If you see an authentication failure, verify `ARCGIS_API_KEY` is set correctly.
- If you hit rate limiting (HTTP 429), retry after waiting or reduce batch size.
