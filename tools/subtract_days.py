# tool: subtract_days
# description: Subtracts N days from a date (YYYY-MM-DD)
# author: @divyanshsinghtomar-ds
# example: subtract_days "2024-07-10" "10" → "2024-06-30"

from datetime import datetime, timedelta


def run(date_str: str, days: str) -> str:
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date_obj - timedelta(days=int(days))
    return new_date.strftime("%Y-%m-%d")
