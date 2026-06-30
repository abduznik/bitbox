# tool: absolute
# description: Returns the absolute value of a number
# author: @Diyaaa-12
# example: absolute "-5" -> "5"
def run(*args) -> str:
    n = float(args[0])
    result = abs(n)
    if result == int(result):
        result = int(result)
    return str(result)