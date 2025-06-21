from heapq import heappush, heappop

N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

pq = []
for a, b in X:
    heappush(pq, (a, b))
    
cand = []
ans = 0
for t in range(1, M + 1):
    while pq:
        a, b = heappop(pq)
        if a <= t:
            heappush(cand, -b)
        else:
            heappush(pq, (a, b))
            break

    if cand:
        v = heappop(cand)
        ans += -v

print(ans)
