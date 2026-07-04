# tool: unique_list
# description: Removes duplicates from a list while preserving order (JSON input)
# author: @Diyaaa-12
# example: unique_list "[1,2,2,3,1,4]" -> "[1, 2, 3, 4]"
import json

def run(*args) -> str:
    input_list = json.loads(args[0])
    seen = []
    for item in input_list:
        if item not in seen:
            seen.append(item)
    return json.dumps(seen)