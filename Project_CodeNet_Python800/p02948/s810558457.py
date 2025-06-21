#template
def inputlist(): return [int(k) for k in input().split()]
#template

N,M = inputlist()
li = []
for i in range(N):
    A,B = inputlist()
    B *= -1
    li.append([A,B])
ans = 0
from heapq import *
li.sort()
k = []
heapify(k)
flag = 0
for i in range(1,M+1):
    if flag == N:
        for t in range(M+1-i):
            ans -= heappop(k)
        break
    while li[flag][0] <= i:
        heappush(k,li[flag][1])
        flag = flag + 1
        if flag == N:
            break
    if len(k)>=1:
        ans -= heappop(k)
print(ans)