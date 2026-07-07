# tool: is_ipv4
# description: Checks if a string is a valid ipv4 address.
# author: @itsmgxb24
# example: is_ipv4 "192.168.1.1" -> "True"
def run(*args) -> str:
    text = args[0]

    parts = text.split(".")
    if len(parts) != 4:
        return "False"

    for part in parts:
        if not part.isdigit():
            return "False"
        # reject leading zeros
        if len(part) > 1 and part[0] == "0":
            return "False"
        if not 0 <= int(part) <= 255:
            return "False"

    return "True"
