# tool: octal_to_decimal
# description: Convert an octal string to binary
# author: @MateiB20
# example: octal_to_binary "12" -> "1010"

def run(octal: str) -> str:
    try:
        return str(bin(int(octal, 8))[2:])
    except ValueError:
        return "Error: Invalid octal number"
