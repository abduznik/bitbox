# tool: max_of_two
# description: Returns the larger of two numbers
# author: @openclaw
# example: max_of_two "3" "7" -> "7"


def run(*args) -> str:
    a = float(args[0])
    b = float(args[1])
    result = max(a, b)
    if result == int(result):
        result = int(result)
    return str(result)
