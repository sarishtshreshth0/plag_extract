from functools import reduce
from operator import mul
import collections
n = int(input())
a = list(map(int, input().split()))
ra = [0]
for i in range(n):
    ra.append(ra[i]+a[i])

def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

ca = collections.Counter(ra)
ans = 0
for item, value in ca.items():
    # print(item, value)
    if value >= 2:
        ans += cmb(value, 2)
# print(ca)
print(ans)