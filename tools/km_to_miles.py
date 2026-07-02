# tool: km_to_miles
# description: Converts kilometers to miles
# author: @openclaw
# example: km_to_miles "10" -> "6.21371"


def run(*args) -> str:
    km = float(args[0])
    miles = km * 0.621371
    return str(round(miles, 5))
