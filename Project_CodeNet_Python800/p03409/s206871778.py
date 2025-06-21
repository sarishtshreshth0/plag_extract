n=int(input())
r=[tuple(map(int,input().split())) for _ in range(n)]
b=[tuple(map(int,input().split())) for _ in range(n)]
r=sorted(r)
b=sorted(b)
for x,y in b:
  p,q=-1,-1
  for i,j in r:
    if i<x and j<y and j>q:p,q=i,j
  if (p,q) in r:r.remove((p,q))
print(n-len(r))