# tool: is_even
# description: Checks if a number is even
# author: @JingliangGao
# example: is_even 4 -> True


def run(*args) -> str:
    if len(args) != 1:
        return "Error: is_even requires exactly one argument"
    try:
        num = int(args[0])
        return str(num % 2 == 0)
    except ValueError:
        return f"Error: '{args[0]}' is not a valid integer"
