# tool: percentage
# description: Calculates what percentage part is of whole
# author: @its-Sohan
# example: percentage "25" "200" -> "12.5"


def run(*args) -> str:
    part, whole = float(args[0]), float(args[1])
    result = (part / whole) * 100
    if result == int(result):
        result = int(result)
    return str(result)
