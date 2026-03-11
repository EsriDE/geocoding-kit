from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

try:
    from dotenv import load_dotenv  # type: ignore
except ImportError:  # pragma: no cover
    def load_dotenv(*args, **kwargs):
        """No-op loader when python-dotenv is not installed."""
        return False


@dataclass(frozen=True)
class ArcGISConfig:
    """ArcGIS Location Platform configuration."""

    api_key: str
    geocode_url: str

    @classmethod
    def from_env(
        cls,
        api_key_env: str = "ARCGIS_API_KEY",
        geocode_url_env: str = "ARCGIS_GEOCODE_URL",
    ) -> "ArcGISConfig":
        """Load configuration from environment variables.

        Loads `.env` if present and then reads required environment variables.
        """

        # Load `.env` if it exists (no-op if missing)
        load_dotenv(override=False)

        api_key = os.getenv(api_key_env) or ""
        if not api_key:
            raise ValueError(
                f"Missing required environment variable `{api_key_env}`. "
                "Set it in your environment or in a `.env` file."
            )

        geocode_url = os.getenv(
            geocode_url_env,
            "https://geocode-api.arcgis.com/arcgis/rest/services/World/GeocodeServer",
        )

        return cls(api_key=api_key, geocode_url=geocode_url)
