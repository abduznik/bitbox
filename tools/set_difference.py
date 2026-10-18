# tool: set_difference
# description: Find elements in the first list that are absent from the second list
# author: @pardhusriparupudi
# example: set_difference "1,2,3" "2,4" -> "1,3"

def run(*args) -> str:
    if len(args) != 2:
        return "Error: Please provide exactly two comma-separated lists."

    list1 = [x.strip() for x in str(args[0]).split(",")]
    list2 = {x.strip() for x in str(args[1]).split(",")}

    result = []
    seen = set()

    for item in list1:
        if item and item not in list2 and item not in seen:
            result.append(item)
            seen.add(item)

    return ",".join(result)
