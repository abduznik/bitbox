# tool: mode_of_list
# description: Find the mode of a list of numbers
# author: @1998LJ
# example: mode_of_list "1,2,2,3" -> "2"

from collections import Counter


def run(*args) -> str:
    if not args:
        return "Error: expected a comma-separated list of numbers"
    val = str(args[0]).strip()
    if not val:
        return "Error: expected a comma-separated list of numbers"

    parts = [p.strip() for p in val.split(",")]
    if any(not p for p in parts):
        return "Error: all elements must be numbers"

    nums = []
    for p in parts:
        try:
            nums.append(float(p) if "." in p else int(p))
        except ValueError:
            return "Error: all elements must be numbers"

    counts = Counter(nums)
    max_freq = max(counts.values())
    modes = [num for num, freq in counts.items() if freq == max_freq]

    # Format output numbers cleanly (remove trailing .0 for whole float numbers)
    formatted = []
    for m in modes:
        if isinstance(m, float) and m.is_integer():
            formatted.append(str(int(m)))
        else:
            formatted.append(str(m))

    return ",".join(formatted)
