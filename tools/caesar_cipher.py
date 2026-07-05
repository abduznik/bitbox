# tool: caesar_cipher
# description: Encodes a string using a Caesar cipher shift
# author: @its-Sohan
# example: caesar_cipher "hello" "3" -> "khoor"


def run(*args) -> str:
    text = args[0]
    shift = int(args[1])
    result = []
    for c in text:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            result.append(chr((ord(c) - base + shift) % 26 + base))
        else:
            result.append(c)
    return "".join(result)
