import math

def run(a: str, b: str) -> str:
  return str(math.gcd(int(a), int(b)) == 1)
