# tool: is_palindrome_number
# description: Checks if a number is a palindrome.
# author: @1998LJ
# example: is_palindrome_number("121") returns "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    if not val:
        return "Error: Argument cannot be empty."

    # Handle optional leading negative sign or validate numeric
    # Negative numbers are generally not palindromes (e.g. -121 != 121-)
    if val.startswith('-'):
        return "False"

    if not val.isdigit():
        return "Error: Argument must be an integer."

    return str(val == val[::-1])
