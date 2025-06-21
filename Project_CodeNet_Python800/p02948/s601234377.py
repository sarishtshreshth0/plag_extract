import heapq
N, M = map(int, input().split())
job = [[] for _ in range(M+1)]
q = []
for i in range(N):
  a, b = map(int, input().split())
  if(a <= M):
    job[a].append(b)
  
ans = 0
for day in range(M+1):
  for value in job[day]:
    heapq.heappush(q, value*(-1))
  if(len(q) > 0):
    ans += heapq.heappop(q)*(-1)
  
print(ans)