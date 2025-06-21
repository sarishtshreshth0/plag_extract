import heapq
N,M = map(int,input().split())
jobs = [ [] for _ in range(M+1) ]
for _ in range(N):
  a,b = map(int,input().split())
  if a <= M:
    jobs[a].append(b)

pq = []
d = 1
res = 0
for _ in range(M-1, -1, -1):
  for b in jobs[d]:
    heapq.heappush(pq, -b)
  if pq:
    res += -heapq.heappop(pq)
  d += 1

print(res)