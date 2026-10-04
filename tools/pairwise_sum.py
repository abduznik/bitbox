# tool: pairwise_sum
# description: Sum corresponding elements of two lists
# author: @abduznik
# example: pairwise_sum "1,2,3" "4,5,6" -> "5,7,9"


def _nums(raw: str):
    values = []
    for part in raw.split(","):
        token = part.strip()
        try:
            values.append(int(token))
        except ValueError:
            values.append(float(token))  # raises ValueError on junk
    return values


def run(*args) -> str:
    if len(args) != 2:
        return "Error: Please provide exactly two arguments."
    try:
        left, right = _nums(args[0]), _nums(args[1])
    except ValueError:
        return "Error: Expected comma-separated numbers"
    if len(left) != len(right):
        return "Error: Lists must be the same length."
    sums = [a + b for a, b in zip(left, right)]
    return ",".join(str(int(v)) if isinstance(v, float) and v.is_integer() else str(v)
                    for v in sums)
