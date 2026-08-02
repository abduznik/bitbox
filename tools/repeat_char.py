# tool: repeat_char
# description: Repeat a character N times
# author: @AshSgDe29071999
# example: repeat_char "*" "5" -> "*****"

def run(*args) -> str:
    char = args[0]
    n = int(args[1])
    if len(char) != 1:
        raise ValueError("char must be a single character")
    if n < 0:
        raise ValueError("n must be non-negative")
    return char * n
