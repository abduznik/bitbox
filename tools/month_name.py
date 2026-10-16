# tool: month_name
# description: Name of the month for a date.
# author: @masyarakatai
# example: month_name "2026-08-15" -> "August"

from datetime import date


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        value = date.fromisoformat(args[0].strip())
    except (AttributeError, ValueError):
        return "Error: Invalid date. Use YYYY-MM-DD format."

    return value.strftime("%B")
