def main():
  n,m=map(int,input().split())
  ab=[list(map(int,input().split())) for _ in range(n)]
  grp=[[]for _ in range(m+1)]
  for a,b in ab:
    if a>m:
      continue
    grp[a].append(b)
  for i,grpi in enumerate(grp):
    grpi.sort()
  import heapq
  maxs=[]
  heapq.heapify(maxs)
  ans=0
  for i in range(1,m+1):
    if len(grp[i])>0:
      heapq.heappush(maxs,[-grp[i].pop(),i])
    if len(maxs)>0:
      v,j=heapq.heappop(maxs)
      ans-=v
      if len(grp[j])>0:
        heapq.heappush(maxs,[-grp[j].pop(),j])

  print(ans)
if __name__=='__main__':
  main()