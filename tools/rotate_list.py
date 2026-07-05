# tool: rotate_list
# description: Rotates a list by n positions to the right (JSON input)
# author: @its-Sohan
# example: rotate_list "[1,2,3,4,5]" "2" -> "[4, 5, 1, 2, 3]"


import json


def run(*args) -> str:
    lst = json.loads(args[0])
    n = int(args[1]) % len(lst) if lst else 0
    result = lst[-n:] + lst[:-n] if n else lst
    return json.dumps(result)
