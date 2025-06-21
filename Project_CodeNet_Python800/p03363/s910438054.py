import itertools
from collections import Counter

n = int(input())
al = list(map(int, input().split()))

arr = [0]
arr += list(itertools.accumulate(al))
c = Counter(arr)
ans = 0

for v in c.values():
    ans += v * (v - 1) // 2  # vC2

print(ans)
