# tool: week_of_year
# description: returns the ISO week number for a date (YYYY-MM-DD)
# author: @Solaris-star
# example: week_of_year "2020-01-01" -> "1"

from datetime import date


def run(*args) -> str:
    if not args:
        return "Error: expected a date YYYY-MM-DD"
    try:
        d = date.fromisoformat(args[0])
    except ValueError:
        return f"Error: invalid date {args[0]
