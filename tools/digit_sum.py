# tool: digit_sum
# description: Calculate the sum of digits of a number
# author: @AashishGupta2007
# example: digit_sum "12345" -> "15"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    num = args[0].lstrip("-")

    if num == "":
        return "Error: Please provide a non-empty input."

    if not num.isdigit():
        return "Error: Please provide a numeric input."

    sumi = 0
    for i in num:
        sumi += int(i)

    return str(sumi)