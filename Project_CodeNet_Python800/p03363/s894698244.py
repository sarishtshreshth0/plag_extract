import itertools
from collections import Counter

n = int(input())
a = list(map(int,input().split()))
arr = [0]
arr += list(itertools.accumulate(a))
ans = 0

c = Counter(arr)
for v in c.values():
    if v > 1:
        ans += v * (v - 1) // 2

print(ans)
