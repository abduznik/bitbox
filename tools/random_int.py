# tool: random_int
# description: generates a random integer between two given numbers
# author: @navaneethsankar07
# example: random_int "1" "10" -> "7"


import random


def run(*args) -> str:
    if len(args) != 2:
        return "Error: Please provide exactly two arguments (min and max)."

    try:
        min_val = int(args[0])
        max_val = int(args[1])
    except ValueError:
        return "Error: Arguments must be integers."
    
    if min_val > max_val:
        return "Error: Minimum value cannot be greater than maximum value."

    return str(random.randint(min_val, max_val))
