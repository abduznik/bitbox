# tool: is_weekend
# description: Checks if a date falls on a weekend.
# author: @navaneethsankar07
# example: is_weekend("2024-06-29") returns "True"

from datetime import date


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        input_date = date.fromisoformat(args[0])
    except ValueError:
        return "Error: Invalid date. Use YYYY-MM-DD format."

    return str(input_date.weekday() >= 5)
