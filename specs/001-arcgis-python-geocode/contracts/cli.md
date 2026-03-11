# CLI Contract: geocode_addresses.py

This document defines the user-facing command-line interface for the example geocoding script.

## Command

```bash
python examples/geocode_addresses.py --input <INPUT_CSV> --output <OUTPUT_CSV> [options]
```

## Arguments

- `--input <INPUT_CSV>` (required): Path to the input CSV file containing addresses to geocode.
- `--output <OUTPUT_CSV>` (required): Path where the output CSV file will be written.

## Options

- `--key <API_KEY>` (optional): ArcGIS Location Platform API key. If omitted, the script reads `ARCGIS_API_KEY` from the environment or `.env`.
- `--batch-size <N>` (optional): Number of addresses to send per request (default: 100).
- `--retry` (optional): Enable a simple retry/backoff strategy for transient failures (e.g., HTTP 429 rate limiting).
- `--verbose` (optional): Print progress and debug info to stderr.

## Output Contract

The output CSV contains one row per input address, with columns including (but not limited to):

- `id`
- `input_address`
- `matched_address`
- `latitude`
- `longitude`
- `score`
- `match_type` (e.g. `PointAddress`)
- `match_status` (e.g., `M`, `T`, `U`)

## Errors

The script should exit with a non-zero status when:

- Authentication fails (invalid/expired key)
- Required arguments are missing
- The input file cannot be read or the output file cannot be written

When possible, the script should continue processing remaining rows even if some addresses fail to geocode.
