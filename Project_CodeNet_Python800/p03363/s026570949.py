import sys, itertools
from collections import Counter

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))
S = [0] + list(itertools.accumulate(A))

C = Counter(S)

res = 0
for v in C.values():
    res += v * (v - 1) // 2

print(res)
