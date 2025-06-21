import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter
from itertools import accumulate

n, *a = map(int, read().split())
ans = 0
for v in Counter([0] + list(accumulate(a))).values():
    ans += v * (v - 1) // 2
print(ans)
