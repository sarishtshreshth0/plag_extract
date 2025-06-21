import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def S(): return sys.stdin.readline().rstrip()

N,M = map(int,S().split())

AB = []
for i in range(N):
    a,b = LI()
    AB.append((a,-b))

from operator import itemgetter

AB = sorted(AB,key = itemgetter(0))

import heapq

L = []
heapq.heapify(L)

ans = 0
r = 0
for i in range(1,M+1):
    for j in range(r,N):
        if AB[j][0] == i:
            heapq.heappush(L,AB[j][1])
        else:
            r = j
            break
    if len(L) >= 1:
        ans -= heapq.heappop(L)

print(ans)