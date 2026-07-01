# tool: km_to_miles
# description: Converts kilometers to miles
# author: @insisong
# example: km_to_miles "10" → "6.21371"


def run(*args) -> str:
    kilometers = float(args[0])
    miles = round(kilometers * 0.621371, 5)
    return str(miles)
