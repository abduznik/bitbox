# tool: zip_lists
# description: Zips two lists into a list of pairs (JSON input)
# author: @its-Sohan
# example: zip_lists "[1,2,3]" "[4,5,6]" -> "[[1, 4], [2, 5], [3, 6]]"


import json


def run(*args) -> str:
    list1 = json.loads(args[0])
    list2 = json.loads(args[1])
    result = list(zip(list1, list2))
    return json.dumps(result)
