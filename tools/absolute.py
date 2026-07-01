# tool: absolute
# description: Returns the absolute value of a number
# author: @insisong
# example: absolute "-5" → "5"


def run(*args) -> str:
    value = abs(float(args[0]))
    return str(int(value)) if value.is_integer() else str(value)
