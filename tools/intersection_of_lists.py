# tool: intersection_of_lists
# description: Find common elements in two lists
# author: @zynnqt
# example: intersection_of_lists "1,2,3" "2,3,4" -> "2,3"


def run(*args) -> str:
    list1 = [x.strip() for x in args[0].split(",")]
    list2 = [x.strip() for x in args[1].split(",")]
    common = [x for x in list1 if x in list2]
    return ",".join(dict.fromkeys(common))
