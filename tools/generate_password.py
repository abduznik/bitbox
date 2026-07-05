# tool: generate_password
# description: Generates a random password with a given length
# author: @its-Sohan
# example: generate_password "12" -> "aB3$kL9#xQ2!"


import random
import string


def run(*args) -> str:
    length = int(args[0]) if args else 16
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.SystemRandom().choice(chars) for _ in range(length))
    return password
