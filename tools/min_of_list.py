# tool: min_of_list
# description: Find the minimum in a list of comma-separated numbers
# author: @isaakchoi
# example: min_of_list "3,1,4,1,5" -> "1"

def run(*args) -> str:
    
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")

    text = args[0]

    numbers = [float(x) for x in text.split(",")]
    
    return str(min(numbers))
