# tool: abs_diff
# description: Calculate the absolute difference between two numbers
# author: @isaakchoi
# example: abs_diff "3" "7" -> "4"

def run(*args) -> str:
    
    # NOTE - Only operates on integers. Given floating point numbers are allowed truncated.
    
    if len(args) != 2:
        raise ValueError("Requires exactly two arguments: num1 and num2.")

    num1 = int(args[0])
    num2 = int(args[1])

    return str(abs(num1 - num2))
