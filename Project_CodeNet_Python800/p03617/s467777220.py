import heapq
from collections import defaultdict, deque
from math import ceil, factorial
from fractions import gcd
import sys

sys.setrecursionlimit(10 ** 7)
INF = float("inf")
MOD = 10 ** 9 + 7

si = lambda: input().strip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
smii = lambda: sorted(map(int, input().split()))


Q, H, S, D = mii()
N = ii()

tea = [
    (Q, 0.25),
    (H, 0.5),
    (S, 1),
    (D, 2),
]
tea.sort(key=lambda x: x[0] / x[1])

ans = 0
remaining = N
for i in range(4):
    p, q = tea[i]
    d, m = map(int, divmod(remaining, q))
    if d == 0:
        continue
    ans += d * p
    remaining = m

print(int(ans))
