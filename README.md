# geocoding-kit
A small repo of examples and best-practices for working with geocoding APIs.

## Getting Started

### Prerequisites

- [ArcGIS Location Platform](https://location.arcgis.com)
- Python 3.11+

### Installation

You can set up the project using either a traditional Python virtual environment **or** the `uv` tool.

## Option A: Standard Python Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/EsriDE/geocoding-kit.git
   cd geocoding-kit
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Example: Geocode a list of addresses

1. Copy `.env.example` to `.env` and set your ArcGIS API key:
   ```bash
   cp .env.example .env
   # edit .env and set ARCGIS_API_KEY
   ```
2. Run the example script:
   ```bash
   python examples/geocode_addresses.py --input examples/addresses.csv --output examples/results.csv
   ```

3. Inspect the output:
   ```bash
   cat examples/results.csv
   ```

## Option B: Using uv (recommended for fast, isolated environments)

1. Clone the repository:
   ```bash
   git clone https://github.com/EsriDE/geocoding-kit.git
   cd geocoding-kit

2. Create and sync the environment:
   ```bash
   uv sync
   ```

## Example: Geocode a list of addresses

1. Copy `.env.example` to `.env` and set your ArcGIS API key:
   ```bash
   cp .env.example .env
   # edit .env and set ARCGIS_API_KEY
   ```
2. Run via uv run:
   ```bash
   uv run examples/geocode_addresses.py --input examples/addresses.csv --output examples/results.csv
   ```

3. Inspect the output:
   ```bash
   cat examples/results.csv
   ```

## Feature: ArcGIS API for Python Geocoding Example

This repo includes a complete example feature implemented using the [`001-arcgis-python-geocode`](/specs/001-arcgis-python-geocode/spec.md), and [`002-add-geocode-notebook`](/specs/002-add-geocode-notebook/spec.md) specification.

Key parts:

- [`examples/geocode_addresses.py`](examples/geocode_addresses.py) — runnable script that reads a CSV, calls geocode, and writes results.
- [`examples/geocode_notebook.ipynb`](examples/geocode_notebook.ipynb) — runnable jupyter notebook that reads a CSV, calls geocode, and displays the results in a map view.
- `src/geocoding_kit/` — supporting library (config, models, geocoding logic).
- `tests/` — unit + integration tests verifying behavior.
- `specs/` — spec, implementation plan, and task tracking.

### Run a simple interactive cli

The CLI is intentionally kept minimal and uses the default geocoding parameters provided by ArcGIS Location Platform. It is designed for quick, one‑off lookups using single‑line, well‑formed addresses (ideally including postal code, city, and country).
If you need to handle:

- custom or advanced geocoding parameters,
- incomplete or malformed address strings,
- multi-field input structures, or
- edge cases requiring fine‑tuned locator behavior,

Please visit the technical [geocoding guide](https://developers.arcgis.com/documentation/mapping-and-location-services/geocoding/) for the full set of capabilities and parameter options.

```bash
uv run cli --help

usage: cli [-h] [--key KEY] [-v]

Python shell for exploring ArcGIS Location Platform geocoding services

options:
  -h, --help     show this help message and exit
  --key KEY      ArcGIS Location Platform API key. If omitted, reads ARCGIS_API_KEY from the environment or .env.
  -v, --verbose  Enable verbose output

USAGE EXAMPLE:
  Interactive mode (prompts for address) with verbose output:
    cli --verbose

For more information, visit https://developers.arcgis.com/documentation/mapping-and-location-services/geocoding/
```

```bash
ℹ  Entering interactive mode. Type 'quit' to exit.


Geocoding Shell - Enter an address to geocode
--------------------------------------------------------------------------------
Address: Adenauerallee 206, 53113 Bonn, Deutschland
================================================================================
Address:         Adenauerallee 206, 53113 Bonn, Deutschland
Coordinates:     (7.115907392984, 50.720188394524)
Matched Address: Adenauerallee 206, 53113, Bonn, Gronau, Nordrhein-Westfalen
Score:           100.0
Status:          M
Match Type:      PointAddress
================================================================================

Geocoding Shell - Enter an address to geocode
--------------------------------------------------------------------------------
Address:
```

# References

For further information, walkthroughs, and community discussions, explore the following resources:

- **Developer Guide (Walkthroughs & Concepts)**  
  https://developers.arcgis.com/documentation/mapping-and-location-services/geocoding/

- **Geocoding Service REST API Reference**  
  https://developers.arcgis.com/rest/geocode/

- **Esri Community Forum for REST APIs**  
  https://community.esri.com/t5/arcgis-rest-apis-and-services/ct-p/arcgis-rest-api


## Contributing

We welcome contributions from anyone and everyone. Please see our [guidelines for contributing](CONTRIBUTING.md).

## License

This project is licensed under the Apache V2 License - see the [LICENSE](LICENSE) file for details.
