# tool: decimal_to_octal
# description: Converts a decimal number to its octal representation.
# author: @navaneethsankar07
# example: decimal_to_octal("42") returns "52"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        number = int(args[0])
    except ValueError:
        return "Error: Input must be an integer."

    if number < 0:
        return "-" + oct(abs(number))[2:]

    return oct(number)[2:]
