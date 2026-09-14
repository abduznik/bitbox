# tool: levenshtein_edit_distance
# description: Levenshtein distance between two comma-separated strings
# author: @00200200
# example: levenshtein_edit_distance "kitten,sitting" -> "3"


def run(*args) -> str:
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")
    if "," not in args[0]:
        raise ValueError("Expected two strings separated by a comma")
    left, right = args[0].split(",", 1)
    if len(left) < len(right):
        left, right = right, left
    previous = list(range(len(right) + 1))
    for row, left_char in enumerate(left, 1):
        current = [row]
        for column, right_char in enumerate(right, 1):
            current.append(
                min(
                    current[-1] + 1,
                    previous[column] + 1,
                    previous[column - 1] + (left_char != right_char),
                )
            )
        previous = current
    return str(previous[-1])
