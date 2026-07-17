# tool: decimal_to_binary
# description: Converts a decimal integer to its binary string representation
# author: @Ayush-0918
# example: decimal_to_binary "10" -> "1010"


def run(*args) -> str:
    n = int(args[0])
    return bin(n)[2:]
