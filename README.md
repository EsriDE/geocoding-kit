# geocoding-kit
A small repo of examples and best-practices for working with geocoding APIs.

## Getting Started

### Prerequisites

- [ArcGIS Location Platform](https://location.arcgis.com)
- Python 3.11+

### Installation

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

## Contributing

We welcome contributions from anyone and everyone. Please see our [guidelines for contributing](CONTRIBUTING.md).

## License

This project is licensed under the Apache V2 License - see the [LICENSE](LICENSE) file for details.
