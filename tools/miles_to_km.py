# tool: miles_to_km
# description: Converts miles to kilometers
# author: @ishita-0301
# example: miles_to_km "10" → "16.0934"


def run(*args) -> str:
    miles = float(args[0])
    km = miles * 1.60934
    return str(round(km, 4))
