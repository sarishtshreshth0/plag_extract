ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n,m = mi()
A = []
for _ in range(n):
    a,b = mi()
    A.append([a,b])
A.sort()

import heapq
a = []
ima = 0
ans = 0
for i in range(1,m+1):
    while True:
        if ima == n:
            break
        if A[ima][0] <= i:
            heapq.heappush(a,-A[ima][1])
            ima += 1
        else:
            break
    if a:
        ans += heapq.heappop(a)*-1
print(ans)


