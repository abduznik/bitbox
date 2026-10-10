# tool: is_harshad
# description: Check if a number is a Harshad number.
# author: @CRYPTONIKAV
# example: is_harshad "18" -> "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    try:
        n = int(val)
    except ValueError:
        return f"Error: Invalid integer '{val}'."
    if n < 1:
        return "Error: Expected a positive integer."

    digit_sum = sum(int(d) for d in str(n))
    return str(n % digit_sum == 0)
