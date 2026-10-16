# tool: quarter_of_year
# description: Calendar quarter for a date.
# author: @masyarakatai
# example: quarter_of_year "2026-08-15" -> "Q3"

from datetime import date


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        value = date.fromisoformat(args[0].strip())
    except (AttributeError, ValueError):
        return "Error: Invalid date. Use YYYY-MM-DD format."

    return f"Q{(value.month - 1) // 3 + 1}"
