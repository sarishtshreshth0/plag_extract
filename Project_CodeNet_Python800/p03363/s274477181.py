import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict
from itertools import accumulate

n, *a = map(int, read().split())
dict = defaultdict(int)
ans = 0
for aa in list(accumulate([0] + a)):
    dict[aa] += 1
for v in dict.values():
    ans += v * (v - 1) // 2
print(ans)
