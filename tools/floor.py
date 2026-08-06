# tool: floor
# description: Round a number down to the nearest integer
# author: @isaakchoi
# example: floor "3.8" -> "3"

def run(*args) -> str:

    # NOTE - Accurate results rely on the precision of the input number being representable by python floats.
    
    import math
    
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")

    text = args[0]
    
    return str(math.floor(float(text)))
