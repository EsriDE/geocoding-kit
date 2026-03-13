"""
Command-line interface for the geocoder-kit.
"""

import argparse
import logging
import os
import sys
from typing import List, Optional

from .config import ArcGISConfig
from .geocode import PlatformGeocoder
from .models import ExtendedGeocodeResult, SingleLineAddressInput

logger = logging.getLogger(__name__)


def create_parser() -> argparse.ArgumentParser:
    """
    Create the argument parser for the geocoder CLI.

    Returns:
        ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="cli",
        description="Python shell for exploring ArcGIS Location Platform geocoding services",
        epilog=(
            "USAGE EXAMPLE:\n"
            "  Interactive mode (prompts for address) with verbose output:\n"
            "    cli --verbose\n\n"
            "For more information, visit https://developers.arcgis.com/documentation/mapping-and-location-services/geocoding/"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Positional arguments (none required - interactive by default)
    parser.add_argument(
        "--key",
        help="ArcGIS Location Platform API key. If omitted, reads ARCGIS_API_KEY from the environment or .env.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    return parser

def format_error(title: str, message: str) -> str:
    """
    Format an error message for display.

    Args:
        title: Error title.
        message: Error message.

    Returns:
        Formatted error string.
    """
    lines = [
        "\n" + "!" * 80,
        f"ERROR: {title}",
        "!" * 80,
        message,
        "!" * 80 + "\n",
    ]
    return "\n".join(lines)

def format_info(message: str) -> str:
    """
    Format an info message for display.

    Args:
        message: Info message.

    Returns:
        Formatted info string.
    """
    return f"\nℹ  {message}\n"

def format_result(extended_result: ExtendedGeocodeResult, verbose: bool=False) -> str:
    """
    Format a single geocode response for display.

    Args:
        extended_result: ExtendedGeocodeResult object to format.
        verbose: If True, include more details in the output.

    Returns:
        Formatted string suitable for terminal output.
    """
    result = extended_result.result

    lines = []
    lines.append("=" * 80)
    lines.append(f"Address:        {result.input_address}")
    
    if result.latitude and result.longitude:
        lines.append(f"Coordinates:    ({result.longitude}, {result.latitude})")
    else:
        lines.append(f"Coordinates:    (No location)")
    
    lines.append(f"Score:          {result.score}")
    lines.append(f"Status:         {result.match_status}")
    
    lines.append("=" * 80)

    if verbose:
        lines.append(f"Matched Address: {result.matched_address or 'N/A'}")
        lines.append(f"Match Type:      {result.match_type or 'N/A'}")

        # Print all atributes returned by the geocoding service, if any
        for key, value in extended_result.attributes.items():
            lines.append(f"  {key}: {value}")
                
    return "\n".join(lines)

def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parse command-line arguments.

    Args:
        args: List of arguments to parse (default: sys.argv[1:]).

    Returns:
        Parsed arguments.
    """
    parser = create_parser()
    return parser.parse_args(args)

def prompt_for_address() -> str:
    """
    Prompt user for an address in interactive mode.

    Returns:
        Address string entered by user.
    """
    print("\nGeocoding Shell - Enter an address to geocode")
    print("-" * 80)
    address = input("Address: ").strip()
    return address

def interactive_mode(geocoder: PlatformGeocoder, parsed_args: argparse.Namespace) -> None:
    """
    Run the shell in interactive mode.

    Args:
        geocoder: PlatformGeocoder instance.
        parsed_args: Parsed command-line arguments.
    """
    print("----------------")
    print(format_info("Entering interactive mode. Type 'quit' to exit."))

    while True:
        try:
            address = prompt_for_address()

            if address.lower() in ["quit", "exit", "q"]:
                print(format_info("Goodbye!"))
                break

            if not address:
                print(format_error("Invalid Input", "Address cannot be empty. Try again."))
                continue

            input = SingleLineAddressInput(address=address)
            result = geocoder.single_line_geocode(input)
            print(format_result(result, verbose=parsed_args.verbose))
        except KeyboardInterrupt:
            print("\n" + format_info("Interrupted. Exiting."))
            break
        except Exception as ex:
            logger.exception("Error in interactive mode")
            print(format_error("Error", str(ex)))

def main(args: Optional[List[str]] = None) -> int:
    """
    Main entry point for the geocoder CLI.

    Args:
        args: List of arguments to parse (default: sys.argv[1:]).

    Returns:
        Exit code (0 for success, 1 for error).
    """
    # Parse arguments
    try:
        parsed_args = parse_args(args)

        # Prefer CLI-provided key over env
        if parsed_args.key:
            os.environ["ARCGIS_API_KEY"] = parsed_args.key
    except SystemExit as ex:
        # Is already handled by argparse, just return the code.
        return ex.code or 0

    # Setup logging
    if parsed_args.verbose:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(levelname)s: %(message)s",
        )
    else:
        logging.basicConfig(
            level=logging.INFO,
            format="%(levelname)s: %(message)s",
        )

    # Initialize configuration and client
    try:
        config = ArcGISConfig.from_env()
        logger.debug("Configuration initialized")
    except Exception as ex:
        logger.exception("Error during configuration")
        print(format_error("Configuration Error", str(ex)))
        return 1

    try:
        geocoder = PlatformGeocoder(config)
        logger.debug("Geocoder initialized")
            
        # Interactive mode
        interactive_mode(geocoder, parsed_args)
        return 0
    except Exception as ex:
        return 1


if __name__ == "__main__":
    sys.exit(main())