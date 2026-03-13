# Quickstart: Geocoding with Jupyter Notebook

This quickstart demonstrates how to use the geocoding-kit to geocode addresses using a Jupyter notebook.

## Prerequisites

- Python environment with geocoding-kit installed
- ArcGIS Location Platform account with geocoding capabilities
- Jupyter notebook environment

## Installation

Ensure the required packages are installed:

```bash
pip install -e .
pip install arcgis arcgis-mapping
```

## Running the Notebook

1. Navigate to the examples folder:
   ```bash
   cd examples/
   ```

2. Start Jupyter notebook:
   ```bash
   jupyter notebook
   ```

3. Open `geocode_notebook.ipynb`

4. Execute the cells in order:
   - Cell 1: Import required libraries
   - Cell 2: Load address data from addresses.csv
   - Cell 3: Initialize geocoding service
   - Cell 4: Geocode addresses
   - Cell 5: Display results

## Expected Output

The notebook will display:
- Original addresses from the CSV
- Geocoded results with coordinates
- Match confidence scores
- Visual representation of geocoded locations

## Troubleshooting

- **Import errors**: Ensure all packages are installed
- **Geocoding failures**: Check ArcGIS credentials and API access
- **File not found**: Verify addresses.csv exists in the examples folder

## Next Steps

- Modify the notebook to work with your own address data
- Add mapping visualizations using arcgis-mapping
- Integrate geocoding into your own applications