# tool: decimal_to_words
# description: Spell out a number in English words
# author: @Cosmosynth
# example: decimal_to_words "1234" -> "one thousand two hundred thirty-four"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Provide exactly one argument."
    try:
        n = int(args[0])
    except (TypeError, ValueError):
        return "Error: Provide a valid integer."

    if n == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
            "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["", "thousand", "million", "billion", "trillion"]

    def helper(num):
        if num == 0: return ""
        if num < 20: return ones[num] + " "
        if num < 100: return tens[num // 10] + ("-" + ones[num % 10] if num % 10 else "") + " "
        return ones[num // 100] + " hundred " + helper(num % 100)

    res, i, neg = "", 0, n < 0
    n = abs(n)
    
    while n > 0:
        if n % 1000 != 0:
            res = helper(n % 1000) + (scales[i] + " " if scales[i] else "") + res
        n //= 1000
        i += 1

    return ("negative " + res if neg else res).strip()