import heapq


N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range (N)]

AB.sort()
ans = 0 
q = []
heapq.heapify(q)
idx = 0
for i in range(1,M+1):
    while idx<N and AB[idx][0]<=i:
        heapq.heappush(q, -AB[idx][1])
        idx += 1
    if q:
        p = -heapq.heappop(q)
        ans += p
print(ans)