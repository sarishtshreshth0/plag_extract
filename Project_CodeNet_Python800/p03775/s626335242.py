import math
def resolve():
    n = int(input())
    ans = len(str(n))
    MAX = int(math.sqrt(n))

    for a in range(1, MAX + 1):
        if n % a != 0:
            continue
        b = int(n / a)
        tmp = max(len(str(a)), len(str(b)))
        ans = min(ans, tmp)

    print(ans)
    return

resolve()
