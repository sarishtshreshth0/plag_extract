N, M = map(int, input().split())
AB = [[] for _ in range(M + 10)]
ans = 0
for _ in range(N):
  a, b = map(int, input().split())
  if a > M:
    continue
  AB[a].append(b)
import heapq
reward = []
heapq.heapify(reward)
for i in range(1, M + 1):
  for item in AB[i]:
    heapq.heappush(reward, -item)
  if reward:
    ans -= heapq.heappop(reward)
print(ans)