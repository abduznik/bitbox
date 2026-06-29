# tool: count_vowels
# description: count the number of vowels in a string
# author: @AviDhandhania
# example: count_vowels "hello world" -> "3"


def run(*args) -> str:
    text = args[0].lower().strip()
    count = 0
    for c in text:
        if c in ['a','e','i','o','u']:
            count+=1
    return str(count)
