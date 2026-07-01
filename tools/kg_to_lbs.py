# tool: kg_to_lbs
# description: Converts kilograms to pounds
# author: @ishita-0301
# example: kg_to_lbs "10" → "22.0462"


def run(*args) -> str:
    kg = float(args[0])
    lbs = kg * 2.20462
    return str(round(lbs, 4))
