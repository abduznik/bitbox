# tool: celsius_to_kelvin
# description: Converts Celsius to Kelvin
# author: @openclaw
# example: celsius_to_kelvin "0" -> "273.15"


def run(*args) -> str:
    celsius = float(args[0])
    kelvin = celsius + 273.15
    return str(round(kelvin, 2))
