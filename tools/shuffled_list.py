# tool: shuffled_list
# description: Returns a shuffled copy of a comma-separated list.
# author: @1998LJ
# example: shuffled_list "1,2,3" -> "2,1,3"

import random


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one comma-separated list."

    items = [item.strip() for item in str(args[0]).split(",") if item.strip()]
    random.shuffle(items)
    return ",".join(items)
