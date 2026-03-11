# Implementation Plan: Python ArcGIS Geocoding Example

**Feature Branch**: `001-arcgis-python-geocode` | **Date**: 2026-03-11 | **Spec**: [spec.md](./spec.md)

## Summary

Provide a minimal, copy/paste runnable Python example that reads a CSV list of addresses, calls the ArcGIS Location Platform Geocoding REST endpoint (`geocodeAddresses`) via the official `arcgis` Python module, and writes a results CSV containing matched address, coordinates, and match status.

## Technical Context

- **Language/Version**: Python 3.11+
- **Primary Dependencies**: `arcgis` (ArcGIS API for Python), `python-dotenv` (optional)
- **Input**: CSV file with required columns (`id`, `address`, `postal`, `city`, `country`)
- **Output**: CSV file with geocoding results (including `match_status` and match score)
- **Testing**: `unittest` with mocks for external dependencies
- **Goal**: Provide an easy-to-run example demonstrating authentication, batching, and handling of no-match results.

## Project Structure

- `examples/geocode_addresses.py` — CLI script that reads input CSV, calls the geocoder, and writes output CSV.
- `src/geocoding_kit/` — library code for configuration, models, and geocoding logic.
- `tests/` — unit and integration tests verifying behavior.

## Plan

1. **Implement config loader** (env + optional `.env`) `src/geocoding_kit/config.py`.
2. **Define data models** (`AddressInput`, `GeocodeResult`) in `src/geocoding_kit/models.py`.
3. **Implement geocode wrapper** in `src/geocoding_kit/geocode.py` that calls `batch_geocode` and selects best candidates.
4. **Create example CLI script** `examples/geocode_addresses.py` that reads CSV, calls library, and writes output.
5. **Add tests** covering config, model shape, parsing logic, and CLI behavior (mocking external calls).
6. **Document quickstart** using `README.md` and `specs/.../quickstart.md`.

## Notes

This feature is intended as a minimal onboarding example; it is not meant as a production-grade ETL pipeline.
