# tool: is_past
# description: Checks if a date is in the past.
# author: @navaneethsankar07
# example: is_past("2020-01-01") returns "True"

from datetime import date


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        input_date = date.fromisoformat(args[0])
    except ValueError:
        return "Error: Invalid date. Use YYYY-MM-DD format."

    return str(input_date < date.today())
