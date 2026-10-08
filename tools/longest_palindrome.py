# tool: longest_palindrome
# description: Finds the longest palindromic substring in a given text
# author: Aditya Waghamare
# example: longest_palindrome "forgeeksskeegfor" -> "geeksskeeg"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one text argument."
    
    text = str(args[0])
    if not text:
        return ""

    start = 0
    max_len = 0

    def expand(l: int, r: int) -> int:
        while l >= 0 and r < len(text) and text[l] == text[r]:
            l -= 1
            r += 1
        return r - l - 1

    for i in range(len(text)):
        len1 = expand(i, i)
        lens = expand(i, i + 1)
        length = max(len1, lens)
        if length > max_len:
            max_len = length
            start = i - (length - 1) // 2

    return text[start:start + max_len]
