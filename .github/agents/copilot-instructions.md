# geocoding-kit Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-03-11

## Active Technologies
- Python 3.11+ + `arcgis` (ArcGIS API for Python), `python-dotenv` (optional) (001-arcgis-python-geocode)
- Input: CSV file; output: CSV or stdout (no persistent storage required) (001-arcgis-python-geocode)
- Python 3.x + geocoding-kit, arcgis, arcgis-mapping (002-add-geocode-notebook)
- CSV file (addresses.csv) (002-add-geocode-notebook)

- Python 3.11+ + `arcgis` (ArcGIS API for Python), `typer` (CLI helper, optional), `python-dotenv` (optional) (001-arcgis-python-geocode)

## Project Structure

```text
src/
tests/
```

## Commands

# Run unit tests (uses Python's standard library `unittest`)
python -m unittest discover -s tests

# Run lint/format checks (if configured)
ruff check .

## Code Style

Python 3.11+: Follow standard conventions

## Recent Changes
- 002-add-geocode-notebook: Added Python 3.x + geocoding-kit, arcgis, arcgis-mapping
- 001-arcgis-python-geocode: Added Python 3.11+ + `arcgis` (ArcGIS API for Python), `python-dotenv` (optional)

- 001-arcgis-python-geocode: Added Python 3.11+ + `arcgis` (ArcGIS API for Python), `typer` (CLI helper, optional), `python-dotenv` (optional)

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
