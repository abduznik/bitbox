# tool: contains substring
# description: to check whether a string contains a given substring
# author: @Rahul6700
# example: contains_substring "hello world" "wor" -> "True"

def run(*args) -> str:
    # checks whether 'string' contains 'sub_string'
    # returns a string of the bool result ('True' or 'False')
    string = args[0]
    sub_string = args[1]
    return str(sub_string in string)
