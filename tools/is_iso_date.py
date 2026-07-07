# tool: is_iso_date
# description: Validates whether a string is a valid ISO 8601 date (YYYY-MM-DD)
# author: @Julito-Dev
# example:  "2026-07-07" → "True"

def run(*args) -> str:
    
    date = args[0]
    
    parts = date.split("-")
    
    if len(parts) != 3:
        return "False"
    
    year, month, day = parts
    
    if len(year) != 4 or len(month) !=2 or len(day) != 2:
        return "False"
    
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return "False"
    
    year = int(year)
    month = int(month)
    day = int(day)
    
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days[1] = 29

    if month < 1 or month > 12 or day < 1 or day > days[month - 1]:
        return "False"

    return "True"
