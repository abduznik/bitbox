def run(meters: str) -> str:
    """Convert meters to feet."""
    try:
        meters_val = float(meters)
        feet_val = meters_val * 3.28084
        return str(round(feet_val, 5))
    except ValueError as e:
        raise ValueError(f"Invalid input for meters: {e}")