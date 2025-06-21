import heapq

n, m = map(int, input().split())
memo = [[] for _ in range(m+1)]

for _ in range(n):
    a, b = map(int ,input().split())
    if a <= m:
        memo[a].append(-b)

ans = 0
HQ = []
heapq.heapify(HQ)
for i in range(1, m+1):
    for j in memo[i]:
        heapq.heappush(HQ, j)
    if HQ:
        ans += heapq.heappop(HQ)

print(-ans)