from datetime import datetime, timezone


def run(date_str: str) -> str:
    """Converts a date string (YYYY-MM-DD) to a Unix timestamp."""
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return str(int(dt.timestamp()))
