# tool: modulo
# description: Returns the remainder of dividing two numbers
# author: @Solaris-star
# example: modulo "10" "3" -> "1"

def run(*args) -> str:
    if len(args) != 2:
        return "Error: Expected exactly 2 arguments."
    try:
        a = float(args[0])
        b = float(args[1])
    except ValueError:
        return "Error: Both arguments must be valid numbers."
    if b == 0:
        return "Error: Division by zero."
    result = a % b
    if float(result).is_integer():
        return str(int(result))
    return str(result)
