# tool: clamp
# description: Clamps a number between a min and max value
# author: @its-Sohan
# example: clamp "15" "0" "10" -> "10"


def run(*args) -> str:
    value, min_val, max_val = float(args[0]), float(args[1]), float(args[2])
    result = max(min_val, min(value, max_val))
    if result == int(result):
        result = int(result)
    return str(result)
