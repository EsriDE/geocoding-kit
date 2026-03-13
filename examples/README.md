# Examples

This folder contains a working example script that uses the `geocoding_kit` library to geocode a list of addresses using ArcGIS Location Platform.

## Run the example

1. Ensure you have a valid ArcGIS API key in `ARCGIS_API_KEY` (via environment variable or `.env`).
2. Run the script:

```bash
python examples/geocode_addresses.py --input examples/addresses.csv --output examples/results.csv
```

The output CSV includes the following columns:

- `id` (original input ID)
- `input_address` (as provided)
- `matched_address` (best match from ArcGIS)
- `latitude` / `longitude`
- `score` (match confidence)
- `match_type` (match type)
- `match_status` (`M` / `T` / `U`)

## Run the jupyter notebook example

The `geocode_notebook.ipynb` demonstrates how to use the `geocoding-kit` module with `arcgis` / `arcgis-mapping` to geocode a list of addresses and display the results using a map view.

**Prerequisites:**
- Install dependencies: `pip install arcgis arcgis-mapping` or if `uv` is installed, just use `uv run jupyter lab`
- Set `ARCGIS_API_KEY` in your environment or `.env` file.

![Geocoding results](https://github.com/user-attachments/assets/e81738ff-4711-4320-9283-9e9a228e9f2f)