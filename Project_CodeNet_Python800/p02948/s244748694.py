import sys
input = sys.stdin.readline
n,m = map(int,input().split())
chk = []
for i in range(n):
  a,b =  map(int,input().split())
  if a <= m:
    chk.append((a,b))

from heapq import heappop, heappush
from operator import itemgetter
chk = sorted(chk,key=itemgetter(0),reverse=True)

q = []
ans = 0
for i in range(1, m + 1):
    while chk and chk[-1][0] <= i:
        a,b = chk.pop()
        heappush(q,-b)
    if q:
        ans -= heappop(q)
print(ans)
