import sys
def input():
    return sys.stdin.readline()[:-1]
N,M=map(int,input().split())
l=[[] for i in range(10**5)]
for i in range(N):
    a,b=map(int,input().split())
    l[a-1].append(b)
h=[]
import heapq
a=0
for i in range(M):
    for j in l[i]:
        heapq.heappush(h,-j)
    if h:
        a-=heapq.heappop(h)
print(a)