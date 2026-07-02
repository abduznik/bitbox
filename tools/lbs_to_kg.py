# tool: lbs_to_kg
# description: Converts pounds to kilograms
# author: @yusichen396
# example: lbs_to_kg "22" -> "9.97903"


def run(*args) -> str:
    lbs = float(args[0])
    kg = lbs * 0.45359237
    return str(round(kg, 5))
