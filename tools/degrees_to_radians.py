# tool: degrees_to_radians
# description: Converts an angle from degrees to radians
# author: @shaurya703
# example: degrees_to_radians "180" -> "3.141592653589793"

import math


def run(*args) -> str:
    try:
        degrees = float(args[0])
        return str(math.radians(degrees))
    except (ValueError, IndexError):
        bad = args[0] if args else ""
        return f"Error: '{bad}' is not a valid number"
