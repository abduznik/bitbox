# tool: range_of_list
# description: Find the range (max-min) of a list
# author: @1998LJ
# example: range_of_list "3,1,4,1,5" -> "4"


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

    diff = max(nums) - min(nums)
    if isinstance(diff, float) and diff.is_integer():
        return str(int(diff))
    return str(diff)
