# tool: age_calculator
# description: Calculate a person's age from their birth date
# author: @aishwarya983
# example: age_calculator "2000-08-15" → "25"

from datetime import date, datetime


def run(*args) -> str:
    birth_date = datetime.strptime(args[0], "%Y-%m-%d").date()
    today = date.today()

    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return str(age)