# tool: fahrenheit_to_celsius
# description: Converts Fahrenheit to Celsius
# author: @openclaw
# example: fahrenheit_to_celsius "212" -> "100.0"


def run(*args) -> str:
    fahrenheit = float(args[0])
    celsius = (fahrenheit - 32) * 5 / 9
    return str(round(celsius, 1))
