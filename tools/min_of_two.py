# tool: min_of_two
# description: Returns the smaller of two numbers
# author: @insisong
# example: min_of_two "3" "7" → "3"


def run(*args) -> str:
    a = float(args[0])
    b = float(args[1])
    value = min(a, b)
    return str(int(value)) if value.is_integer() else str(value)
