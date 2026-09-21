# tool: union_of_lists
# description: Returns unique elements from two comma-separated lists.
# author: @1998LJ
# example: union_of_lists "1,2" "3,4" -> "1,2,3,4"


def run(*args) -> str:
    if len(args) != 2:
        return "Error: Please provide exactly two comma-separated lists."

    items = []
    seen = set()
    for value in args:
        for item in str(value).split(","):
            item = item.strip()
            if item and item not in seen:
                seen.add(item)
                items.append(item)

    return ",".join(items)
