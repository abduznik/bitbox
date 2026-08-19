# tool: octal_to_binary
# description: Converts an octal string to its binary string representation
# author: @Solaris-star
# example: octal_to_binary "12" -> "1010"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        value = int(args[0], 8)
    except ValueError:
        return "Error: Input must be a valid octal number."

    return bin(value)[2:]
