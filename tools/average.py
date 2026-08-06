# tool: average
# description: Calculate the average of comma-separated numbers
# author: @isaakchoi
# example: average "1,2,3,4,5" -> "3.0"

def run(*args) -> str:
    
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")

    text = args[0]

    numbers = [float(x) for x in text.split(",")]
    
    return str(sum(numbers) / len(numbers))
