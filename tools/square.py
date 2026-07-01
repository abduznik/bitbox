# tool: square
# description: Returns the square of a number
# author: @insisong
# example: square "5" → "25"


def run(*args) -> str:
    value = float(args[0]) ** 2
    return str(int(value)) if value.is_integer() else str(value)
