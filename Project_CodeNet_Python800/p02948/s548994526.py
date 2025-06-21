import sys
input = sys.stdin.readline
from collections import *
from heapq import *

N, M = map(int, input().split())
d = defaultdict(list)

for _ in range(N):
    A, B = map(int, input().split())
    d[A].append(B)

pq = []
ans = 0

for i in range(M, -1, -1):
    for v in d[M-i]:
        heappush(pq, -v)
    
    if len(pq)>0:
        ans += -heappop(pq)

print(ans)