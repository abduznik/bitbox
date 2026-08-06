# tool: sum_list
# description: Returns the sum of a list of comma delimited numbers, each delimited by a comma.
# author: @isaakchoi
# example: sum_list "1,2,3,4,5" -> "15"

def run(*args) -> str:

    if len(args) != 1:
        raise ValueError("This tool requires exactly one argument: a comma-delimited list of numbers.")
    
    numbers = args[0].split(",")
    
    return str(sum(float(x) if "." in x else int(x) for x in numbers))
