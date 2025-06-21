import heapq
N,M = map(int,input().split())
lis = [[] for i in range(10**5+10)]
for i in range(N):
    A,B = map(int,input().split())
    lis[A-1].append(-B)
ans = 0
d = []
heapq.heapify(d)
for i in range(M):
    for j in lis[i]:
        heapq.heappush(d,j)
    if len(d) > 0:
        ans += heapq.heappop(d)*-1
print(ans)
