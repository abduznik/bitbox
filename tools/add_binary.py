# tool: add_binary
# description: Add two binary strings
# author: @Enard52
# example: add_binary "1010" "11" -> "1101"


def run(*args) -> str:
    if len(args) != 2:
        return "Error: expected 2 binary strings"

    s1 = str(args[0]).strip()
    s2 = str(args[1]).strip()

    if not s1 or not s2:
        return "Error: binary strings cannot be empty"

    if any(c not in "01" for c in s1) or any(c not in "01" for c in s2):
        return "Error: inputs must only contain '0' and '1'"

    num1 = int(s1, 2)
    num2 = int(s2, 2)
    return bin(num1 + num2)[2:]
