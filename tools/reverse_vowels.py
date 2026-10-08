# tool: reverse_vowels
# description: Reverse the vowels in a string
# author: @odemjan
# example: reverse_vowels "hello" -> "holle"


def run(*args) -> str:
    if len(args) != 1 or not isinstance(args[0], str):
        return "Error: expected string argument"

    text = args[0]
    vowels = "aeiouAEIOU"
    characters = list(text)
    left, right = 0, len(characters) - 1

    while left < right:
        while left < right and characters[left] not in vowels:
            left += 1
        while left < right and characters[right] not in vowels:
            right -= 1
        characters[left], characters[right] = characters[right], characters[left]
        left += 1
        right -= 1

    return "".join(characters)
