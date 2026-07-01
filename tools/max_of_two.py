# tool: max_of_two
# description: Returns the larger of two numbers
# author: @insisong
# example: max_of_two "3" "7" → "7"


def run(*args) -> str:
    a = float(args[0])
    b = float(args[1])
    value = max(a, b)
    return str(int(value)) if value.is_integer() else str(value)
