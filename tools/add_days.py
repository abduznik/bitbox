# tool: add_days
# description: Adds N days to a date.
# author: @navaneethsankar07
# example: add_days("2024-06-30", "10") returns "2024-07-10"

from datetime import date, timedelta


def run(*args) -> str:
    if len(args) != 2:
        return "Error: Please provide exactly two arguments."

    try:
        input_date = date.fromisoformat(args[0])
    except ValueError:
        return "Error: Invalid date. Use YYYY-MM-DD format."

    try:
        days = int(args[1])
    except ValueError:
        return "Error: Days must be an integer."

    return (input_date + timedelta(days=days)).isoformat()
