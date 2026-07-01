# tool: cube
# description: Returns the cube of a number
# author: @insisong
# example: cube "3" → "27"


def run(*args) -> str:
    value = float(args[0]) ** 3
    return str(int(value)) if value.is_integer() else str(value)
