# tool: multiply_tool
# description: Multiplies two numbers
# author: @Dhruv-Kapri
# example: multiply "3" "4" -> "12"


def run(*args) -> str:
    if len(args) != 2:
        return "Error: Expected exactly 2 arguments."

    try:
        a = float(args[0])
        b = float(args[1])
    except ValueError:
        return "Error: Both arguments must be valid numbers."
    
    result = (a*b)
    result = int(result) if result.is_integer() else a*b

    return str(result)
