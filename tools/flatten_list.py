# tool: flatten_list
# description: Flattens a nested list one level deep (JSON input)
# author: @Diyaaa-12
# example: flatten_list "[[1,2],[3,4],[5]]" -> "[1, 2, 3, 4, 5]"
import json

def run(*args) -> str:
    input_list = json.loads(args[0])
    result = []
    for item in input_list:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return json.dumps(result)