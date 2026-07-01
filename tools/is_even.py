# tool: is_even
# description: Checks if a number is even
# author: @Bruce191
# example: is_even "2" -> "True"


def run(*args) -> str:
    # args[0] is the first argument, args[1] is the second, etc.
    # Example with two args: text = args[0], length = int(args[1])
    Numberinput = int(args[0])
    return "True" if Numberinput % 2 == 0 else "False"
