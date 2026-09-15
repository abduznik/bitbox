# tool: longest_common_prefix
# description: Finds the longest common prefix of two comma-separated strings.
# author: @1998LJ
# example: longest_common_prefix("flower,flow") returns "fl"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    raw = str(args[0])
    parts = raw.split(",")
    if len(parts) != 2:
        return "Error: Please provide two comma-separated strings (e.g. 'flower,flow')."

    s1, s2 = parts[0], parts[1]
    prefix = []
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            prefix.append(c1)
        else:
            break

    return "".join(prefix)
