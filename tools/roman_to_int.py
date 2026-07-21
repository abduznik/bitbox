# tool: roman_to_int
# description: converts a Roman numeral to an integer
# author: @Solaris-star
# example: roman_to_int "XIV" -> "14"

_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def run(*args) -> str:
    if not args:
        return "Error: expected a Roman numeral"
    s = args[0].upper().strip()
    if not s or any(ch not in _VALUES for ch in s):
        return f"Error: '{args[0]}' is not a valid Roman numeral"
    total = 0
    prev = 0
    for ch in reversed(s):
        value = _VALUES[ch]
        if value < prev:
            total -= value
        else:
            total += value
            prev = value
    return str(total)
