# tool: is_armstrong
# description: Checks if a number is an Armstrong number.
# author: @navaneethsankar07
# example: is_armstrong("153") returns "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        number = int(args[0])
    except ValueError:
        return "Error: Argument must be an integer."

    if number < 0:
        return "False"

    digits = str(number)
    power = len(digits)

    total = sum(int(digit) ** power for digit in digits)

    return str(total == number)
