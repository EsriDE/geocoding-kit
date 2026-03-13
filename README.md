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

This repo includes a complete example feature implemented using the `specs/001-arcgis-python-geocode/` specification.

Key parts:

- `examples/geocode_addresses.py` — runnable script that reads a CSV, calls geocode, and writes results.
- `examples/geocode_notebook.ipynb` — runnable jupyter notebook that reads a CSV, calls geocode, and displays the results in a map view.
- `src/geocoding_kit/` — supporting library (config, models, geocoding logic).
- `tests/` — unit + integration tests verifying behavior.
- `specs/` — spec, implementation plan, and task tracking.

### Run a simple interactive cli

```bash
uv run cli
```

```bash
ℹ  Entering interactive mode. Type 'quit' to exit.


Geocoding Shell - Enter an address to geocode
--------------------------------------------------------------------------------
Address: Adenauerallee 206, 53113 Bonn, Deutschland
================================================================================
Address:        Adenauerallee 206, 53113 Bonn, Deutschland
Coordinates:    (7.115907392984, 50.720188394524)
Score:          100.0
Status:         M
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
