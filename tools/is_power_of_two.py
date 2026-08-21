# tool: is_power_of_two
# description: Check if a number is a power of two
# author: @isaakchoi
# example: is_power_of_two "8" -> "True"

def run(*args) -> str:
    
    # NOTE - Currently only operates within the integer range (powers 2^n where n is a non-negative integer)
    
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")

    text = args[0]
    
    if not text.isdigit():
        raise ValueError("Argument must be a non-negative integer")

    number = int(text)
    
    return str(number != 0 and (number & (number - 1)) == 0)
