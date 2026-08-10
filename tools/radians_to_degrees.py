# tool: radians_to_degrees
# description: Converts an angle from radians to degrees
# author: @shaurya703
# example: radians_to_degrees "3.14159" -> "179.9998"

import math


def run(*args) -> str:
    try:
        radians = float(args[0])
        return str(round(math.degrees(radians), 4))
    except (ValueError, IndexError):
        bad = args[0] if args else ""
        return f"Error: '{bad}' is not a valid number"
