from heapq import *
N,M = map(int,input().split())
l = [[0] for _ in range(M+1)] 
for _ in range(N):
    a, b = map(int, input().split())
    if a<=M:
        l[a].append(b)

ans = 0
h = []

for i in range(1,M+1):
  for j in l[i]:
    heappush(h, -j)
  ans += heappop(h)
ans *= -1
print(ans)