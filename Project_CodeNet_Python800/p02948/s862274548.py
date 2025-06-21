from sys import stdin
import math
import fractions
from collections import deque
from collections import Counter
import itertools
import heapq

readline = stdin.buffer.readline

INF = 10 ** 10

# M日後まで得られる報酬の合計の最大値
N, M = [int(x) for x in readline().split()]

#Ai日後にBiの金
#AB = [tuple(map(int, readline().split())) for _ in range(N)]

jobs = [[] for _ in range(M+1)]

for _ in range(N):
    A, B = [int(x) for x in readline().split()]
    if A <= M:
        jobs[A].append(B)

# priority queue
pq = [] 

ans = 0

# i = 1 to M
for i in range(1, M+1):
    for job in jobs[i]:
        heapq.heappush(pq, -job)
    
    if(pq):
        ans += -heapq.heappop(pq)

print(ans)   
