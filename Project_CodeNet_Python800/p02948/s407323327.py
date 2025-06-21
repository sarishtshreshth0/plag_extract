from heapq import *
from collections import defaultdict
N, M = map(int, input().split())
data = defaultdict(list)
for _ in range(N):
    A, B = map(int, input().split())
    data[A].append(-B)

res = 0
temp = []
for i in range(1,M+1):
    for a in data[i]:
        heappush(temp,a)
    if temp:
        res -= heappop(temp)
print(res)
