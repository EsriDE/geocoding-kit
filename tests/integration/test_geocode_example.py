import csv
import os
import sys
import tempfile
import unittest
from unittest.mock import patch

# Ensure `src/` is on sys.path so `geocoding_kit` can be imported during tests
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT_DIR, "src"))

from geocoding_kit.models import GeocodeResult


class TestGeocodeExampleCLI(unittest.TestCase):
    @patch("examples.geocode_addresses.Geocoder")
    def test_cli_runs_and_generates_output(self, mock_geocoder_class):
        """The CLI should write a results CSV with the expected header columns."""

        # Arrange: stub out geocoding results to avoid network calls.
        dummy_result = GeocodeResult(
            id="0",
            input_address="123 Main St",
            matched_address="123 Main St",
            latitude=34.0,
            longitude=-117.0,
            score=95.0,
            match_type="PointAddress",
            match_status="Matched",
            error=None,
        )
        mock_geocoder = mock_geocoder_class.return_value
        mock_geocoder.geocode.return_value = [dummy_result]

        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        input_csv = os.path.join(repo_root, "examples", "addresses.csv")

        with tempfile.TemporaryDirectory() as tmpdir:
            output_csv = os.path.join(tmpdir, "results.csv")

            # Run the example script via its main() entrypoint.
            from examples import geocode_addresses

            exit_code = geocode_addresses.main([
                "--input",
                input_csv,
                "--output",
                output_csv,
                "--key",
                "fake-key",
            ])

            self.assertEqual(exit_code, 0)
            self.assertTrue(os.path.exists(output_csv))

            with open(output_csv, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.assertIn("input_address", reader.fieldnames)
                self.assertIn("match_status", reader.fieldnames)
                rows = list(reader)
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0]["match_status"], "Matched")
