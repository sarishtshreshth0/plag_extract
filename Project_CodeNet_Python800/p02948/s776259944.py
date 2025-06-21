import heapq
N,M=map(int,input().split())
AB=[list(map(int,input().split())) for _ in range(N)]

AB.sort(reverse=True)
works=[]
heapq.heapify(works)
ans=0
for i in range(1,M+1):
  day=M-i
  latest=i
  while AB and AB[-1][0]<=latest:
    a,b=AB.pop(-1)
    heapq.heappush(works,-b)
  if not works:
    continue
  ans-=heapq.heappop(works)

print(ans)
