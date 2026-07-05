# tool: chunk_list
# description: Splits a list into chunks of size n (JSON input)
# author: @its-Sohan
# example: chunk_list "[1,2,3,4,5]" "2" -> "[[1, 2], [3, 4], [5]]"


import json


def run(*args) -> str:
    lst = json.loads(args[0])
    n = int(args[1])
    chunks = [lst[i:i + n] for i in range(0, len(lst), n)]
    return json.dumps(chunks)
