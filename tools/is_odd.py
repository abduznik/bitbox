# tool: is_odd
# description: Checks if a number is odd
# author: @Diyaaa-12
# example: is_odd "3" -> "True"
def run(*args) -> str:
    n = int(args[0])
    return str(n % 2 != 0)