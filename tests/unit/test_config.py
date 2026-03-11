import os
import sys
import unittest

# Ensure `src/` is on sys.path so `geocoding_kit` can be imported during tests
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT_DIR, "src"))

from geocoding_kit.config import ArcGISConfig


class TestArcGISConfig(unittest.TestCase):
    def test_from_env_success(self):
        os.environ["ARCGIS_API_KEY"] = "fake-key"
        config = ArcGISConfig.from_env()
        self.assertEqual(config.api_key, "fake-key")
        self.assertIn("GeocodeServer", config.geocode_url)

    def test_from_env_missing_key_raises(self):
        os.environ.pop("ARCGIS_API_KEY", None)
        with self.assertRaises(ValueError):
            ArcGISConfig.from_env()
