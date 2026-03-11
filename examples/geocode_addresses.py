"""Example script: geocode a list of addresses using ArcGIS Location Platform.

This script is intentionally minimal and runnable as a copy/paste example.

Usage:
    python examples/geocode_addresses.py --input addresses.csv --output results.csv

The script reads an input CSV with a column named `address` and writes a CSV with geocoding
results including latitude/longitude and match score.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from typing import List, Optional

# Ensure the local `src/` package is importable when running this script directly.
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT_DIR, "src"))

from geocoding_kit.config import ArcGISConfig
from geocoding_kit.geocode import GeocodeResult, PlatformGeocoder
from geocoding_kit.models import AddressInput


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Geocode a list of addresses using ArcGIS Location Platform.")

    parser.add_argument("--input", required=True, help="Path to input CSV containing the addresses.")
    parser.add_argument("--output", required=True, help="Path to output CSV to write results.")
    parser.add_argument(
        "--key",
        help="ArcGIS API key. If omitted, reads ARCGIS_API_KEY from the environment or .env.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=100,
        help="Number of addresses to send per request (default: 100).",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print progress and debug information to stderr.",
    )

    return parser.parse_args(argv)


def _read_input_csv(path: str) -> List[AddressInput]:
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Input file not found: {path}")

    with open(path, newline="", encoding="utf-8") as in_stream:
        reader = csv.DictReader(in_stream)
        required_columns = {"id", "address", "postal", "city", "country"}
        for col in required_columns:
            if col not in reader.fieldnames:
                raise ValueError(f"Input CSV must contain a '{col}' column.")

        addresses: List[AddressInput] = []
        for idx, row in enumerate(reader):
            for col in required_columns:
                if not row.get(col) or not row[col].strip():
                    raise ValueError(f"Row {idx} is missing a value for required column '{col}'.")
            
            addresses.append(AddressInput(
                id=int(row.get("id")), 
                address=row.get("address") or "", 
                postal=row.get("postal") or "", 
                city=row.get("city") or "", 
                country=row.get("country") or ""))

    return addresses


def _write_output_csv(path: str, results: List[GeocodeResult]) -> None:
    fieldnames = [
        "id",
        "input_address",
        "matched_address",
        "latitude",
        "longitude",
        "score",
        "match_type",
        "match_status"
    ]

    with open(path, "w", newline="", encoding="utf-8") as out_stream:
        writer = csv.DictWriter(out_stream, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(
                {
                    "id": result.id,
                    "input_address": result.input_address,
                    "matched_address": result.matched_address or "",
                    "latitude": result.latitude if result.latitude is not None else "",
                    "longitude": result.longitude if result.longitude is not None else "",
                    "score": result.score if result.score is not None else "",
                    "match_type": result.match_type or "",
                    "match_status": result.match_status
                }
            )


def main(argv: Optional[List[str]] = None) -> int:
    args = _parse_args(argv)

    if args.verbose:
        print(f"Loading configuration (key override: {bool(args.key)})", file=sys.stderr)

    # Prefer CLI-provided key over env
    if args.key:
        os.environ["ARCGIS_API_KEY"] = args.key

    try:
        config = ArcGISConfig.from_env()
    except Exception as ex:
        print(f"Configuration error: {ex}", file=sys.stderr)
        return 1

    if args.verbose:
        print(f"Reading input addresses from {args.input}", file=sys.stderr)

    try:
        inputs = _read_input_csv(args.input)
    except Exception as ex:
        print(f"Failed to read input CSV: {ex}", file=sys.stderr)
        return 1

    if not inputs:
        print("No valid addresses found in input file. Exiting.", file=sys.stderr)
        return 0

    geocoder = PlatformGeocoder(config)
    try:
        results = geocoder.geocode(inputs, batch_size=args.batch_size)
    except Exception as ex:
        print(f"Geocoding failed: {ex}", file=sys.stderr)
        return 1

    if args.verbose:
        matched = sum(1 for r in results if r.match_status == "Matched")
        print(f"Geocoding complete: {matched}/{len(results)} matched", file=sys.stderr)

    try:
        _write_output_csv(args.output, results)
    except Exception as ex:
        print(f"Failed to write output CSV: {ex}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
