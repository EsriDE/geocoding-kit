import csv
import os
import unittest

from geocoding_kit.geocode import PlatformGeocoder
from geocoding_kit.models import AddressInput


class TestSampleAddressGeocode(unittest.TestCase):
    def test_parse_response_for_sample_address(self):
        # Use an actual sample address from the example CSV to validate parsing.
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        sample_csv = os.path.join(repo_root, "examples", "addresses.csv")

        with open(sample_csv, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            first_row = next(reader)

        address_input = AddressInput(
            id=int(first_row["id"]),
            address=first_row["address"],
            postal=first_row["postal"],
            city=first_row["city"],
            country=first_row["country"],
        )

        # Craft a fake ArcGIS response that matches the sample address.
        response = [
            {
                "address": address_input.address,
                "location": {"x": 13.404954, "y": 52.520008},
                "score": 95.0,
                "attributes": {
                    "ResultID": address_input.id,
                    "Match_addr": address_input.address,
                    "Addr_type": "PointAddress",
                    "Status": "M",
                },
            }
        ]

        results = PlatformGeocoder(config=None)._parse_response(response, [address_input])  # type: ignore[arg-type]

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, address_input.id)
        self.assertEqual(results[0].match_status, "M")
        self.assertEqual(results[0].matched_address, address_input.address)
        self.assertEqual(results[0].score, 95.0)
