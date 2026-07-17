# tool: day_of_week
# description: Returns the day of the week for a given date in YYYY-MM-DD format
# author: @navaneethsankar07
# example: day_of_week("2023-09-15") returns "Friday"


from datetime import datetime


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        date = datetime.strptime(args[0], "%Y-%m-%d")
    except ValueError:
        return "Error: Invalid date format. Use YYYY-MM-DD."

    return date.strftime("%A")