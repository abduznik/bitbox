# tool: is_credit_card
# description: validates a number using the Luhn algorithm (credit card check)
# author: @Solaris-star
# example: is_credit_card "4111111111111111" -> "true"

import re


def run(*args) -> str:
    if not args:
        return "Error: expected a card number"
    digits = re.sub(r"[\s-]", "", args[0])
    if not digits.isdigit() or len(digits) < 2:
        return "false"

    total = 0
    reverse = digits[::-1]
    for i, ch in enumerate(reverse):
        n = int(ch)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return "true" if total % 10 == 0 else "false"
