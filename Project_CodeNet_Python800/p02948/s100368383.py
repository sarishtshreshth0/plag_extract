import heapq as hp
n,m=map(int,input().split())
AB=[[] for i in range(m+1)]

for i in range(n):
  a,b=map(int,input().split())
  if a<=m:
    AB[a].append(-b)

ans=0
l=[]
hp.heapify(l)
for ab in AB:
  for t in ab:
    hp.heappush(l,t)
  if len(l)>0:
    ans-=hp.heappop(l)
print(ans)

