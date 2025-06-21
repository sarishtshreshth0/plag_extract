import heapq

N,M=map(int,input().split())
jobs=[[] for i in range(M)]

for i in range(N):
  a,b=map(int,input().split())
  if a>M:
    continue
  else:
    jobs[M-a].append(b)
ans=0
l=[]
for i in range(M-1,-1,-1):
  for j in jobs[i]:
    heapq.heappush(l,-j)
  if len(l):
    ans+=-heapq.heappop(l)
print(ans)