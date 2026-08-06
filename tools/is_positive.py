# tool: is_positive
# description: Returns whether the input number is positive
# author: @isaakchoi
# example: is_positive "5" -> "True"

def run(*args) -> str:
    
    if len(args) != 1:
        raise ValueError("Requires exactly one argument.")
    
    return str(float(args[0]) > 0)
