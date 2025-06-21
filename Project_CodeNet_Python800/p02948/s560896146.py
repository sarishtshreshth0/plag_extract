import heapq
N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
day = {i+1:[] for i in range(M)}
for a, b in ab:
  if a <= M:
    day[a] += [-b]

q = []
ans = 0
for i in range(M):
  for b in day[i+1]:
    heapq.heappush(q, b)
  if len(q) > 0:
    ans += -1 * heapq.heappop(q)
print(ans)