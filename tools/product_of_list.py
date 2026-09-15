# tool: product_of_list
# description: Computes the product of a comma-separated list of numbers.
# author: @1998LJ
# example: product_of_list("1,2,3,4") returns "24"

import math


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    if not val:
        return "Error: Argument cannot be empty."

    parts = [p.strip() for p in val.split(",") if p.strip()]
    if not parts:
        return "Error: List cannot be empty."

    nums = []
    for p in parts:
        try:
            nums.append(int(p) if "." not in p else float(p))
        except ValueError:
            return f"Error: Invalid number '{p}'."

    prod = 1
    for n in nums:
        prod *= n

    return f"{prod:g}" if isinstance(prod, float) else str(prod)
