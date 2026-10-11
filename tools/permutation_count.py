def run(n: str, r: str) ->str:
    n, r= int(n), int(r)
    ans = 1
    for i in range(n, n-r, -1):
        ans *= 1
    return str(ans)
