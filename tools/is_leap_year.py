# tool: is_leap_year
# description: Checks whether a given year is a leap year
# author: @fkskfana
# example: is_leap_year "2024" -> "True"

def run(*args) -> str:
    # args[0] is the year passed as a string
    year = int(args[0])
    
    # A leap year is divisible by 4, but not 100 unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "True"
    else:
        return "False"
        
