#import bisect
import heapq
from collections import deque
n,m = map(int,input().split())
ab=[]
for i in range(n):
    ab.append(list(map(int,input().split())))

lis = [[]for i in range(m)]

for i in range(n):
    if ab[i][0]<=m:
        lis[ab[i][0]-1].append(ab[i][1])

pys = []
heapq.heapify(pys)
sum = 0
for i in range(m):
    tmp = lis[i]
    if tmp:
        for j in tmp:
            heapq.heappush(pys,-j)
    if pys:
        sum-=heapq.heappop(pys)

print(sum)
