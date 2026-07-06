# tool: int_to_roman
# description: Converts an integer (1–3999) to a Roman numeral string
# author: @AminodinAkbari
# example: int_to_roman "14" → "XIV"

VALUES_SYMBOLS = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
    (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
    (1, "I"),
]


def run(*args) -> str:
    """Convert an integer to a Roman numeral string.

    Accepts a string-represented integer between 1 and 3999 (inclusive)
    and returns its Roman numeral equivalent using standard subtractive
    notation (e.g., 4 -> IV, 9 -> IX, 40 -> XL).

    Args:
        *args: Variable-length argument list. The first element is expected
               to be a string representation of an integer.

    Returns:
        The Roman numeral string, or an error message if input is invalid
        or out of range.
    """
    if not args:
        return "Error: missing input number"

    try:
        n = int(args[0])
    except (ValueError, TypeError):
        return f"Error: '{args[0]}' is not a valid integer"

    # Standard Roman numerals use only M (1000) as the highest symbol.
    # With subtractive notation, the maximum representable value is 3999 (MMMCMXCIX).
    # Numbers >= 4000 require a vinculum (bar) notation, which is beyond this tool's scope.
    if not (1 <= n <= 3999):
        return "Error: number must be between 1 and 3999"

    roman_parts = []
    for value, symbol in VALUES_SYMBOLS:
        if n == 0:
            break
        count, n = divmod(n, value)
        roman_parts.append(symbol * count)

    return "".join(roman_parts)