# tool: symmetric_difference
# description: Elements in either list but not both
# author: @Subham-entity
# example: symmetric_difference "1,2" "2,3" -> "1,3"

def run(*args) -> str:
    if len(args) != 2:
        return "Error: Please provide exactly two comma-separated lists."
    
    set_a = set(item.strip() for item in str(args[0]).split(",") if item.strip())
    set_b = set(item.strip() for item in str(args[1]).split(",") if item.strip())
    
    result_set = set_a ^ set_b
    return ",".join(sorted(result_set))