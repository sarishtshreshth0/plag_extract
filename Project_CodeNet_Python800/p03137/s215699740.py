import math
import collections
import fractions
import itertools

def solve():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
    else:
        diff = [abs(x[i] - x[i+1]) for i in range(m-1)]
        diff.sort(reverse=True)
        ans = sum(diff)
        for i in range(n-1):
            ans -= diff[i]
        print(ans)
    return 0

if __name__ == "__main__":
    solve()