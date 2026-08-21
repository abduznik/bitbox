# tool: is_negative
# description: Returns whether the input number is negative
# author: @isaakchoi
# example: is_negative "-5" -> "True"

def run(*args) -> str:
    
    if len(args) != 1:
        raise ValueError("Requires exactly one argument.")
    
    return str(float(args[0]) < 0)
