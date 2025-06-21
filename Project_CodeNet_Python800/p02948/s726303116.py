from heapq import heappush, heappop
N, M = map(int, input().split())
D = {i+1: [] for i in range(M)}
for _ in range(N):
  A, B = map(int, input().split())
  if A <= M:
    D[A].append(B)
rew = 0
pq = []
for i in range(M):
  for j in D[i+1]:
    heappush(pq, -j)
  if pq != []:
    rew += -heappop(pq)
print(rew)