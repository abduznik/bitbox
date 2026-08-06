# tool: ceil
# description: Round a number up to the nearest integer
# author: @isaakchoi
# example: ceil "3.2" -> "4"

def run(*args) -> str:

    import math
    
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")

    text = args[0]
    
    return str(math.ceil(float(text)))
