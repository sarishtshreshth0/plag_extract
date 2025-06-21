import sys
import math
import bisect
import heapq
stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

N,M=nm()
Bl=[[] for i in range(10**5+5)]

for i in range(N):
    A,B=nm()
    Bl[A].append(-B)

now=[]
if(Bl[0]!=[]):
    for i in range(len(Bl[0])):
        heapq.heappush(now,Bl[0][i])

ans=0
for i in range(1,M+2):
    if(now!=[]):
        max_val=heapq.heappop(now)
        ans+=max_val
    if(Bl[i]!=[]):
        for j in range(len(Bl[i])):
            heapq.heappush(now,Bl[i][j])

print(-ans)
