# tool: roman_to_int
# description: Converts a Roman numeral string to an integer
# author: @its-Sohan
# example: roman_to_int "XIV" -> "14"


def run(*args) -> str:
    roman = args[0].upper()
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for c in reversed(roman):
        curr = values[c]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    return str(total)
