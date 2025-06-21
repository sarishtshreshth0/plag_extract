N,M = map(int,input().split())
t = [[0] for _ in range(M+1)]
for _ in range(N):
    a,b = map(int,input().split())
    if a<=M:
        t[a].append(b)
import heapq
A=[-i for i in t[1]]
heapq.heapify(A)
ans = 0
for i in range(1,M+1):
    maxi = heapq.heappop(A)
    ans -= maxi
    if i+1<=M:
        for k in t[i+1]:
            heapq.heappush(A,-k)
print(ans)