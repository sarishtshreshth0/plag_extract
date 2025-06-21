n,m=map(int,input().split())

par=[i for i in range(n)]
size=[1]*n

def find(x):
  if par[x]==x:
    return x
  else:
    par[x]=find(par[x])
    return par[x]
def union(a,b):
  x=find(a)
  y=find(b)
  if x!=y:
    if size[x]<size[y]:
      par[x]=par[y]
      size[y]+=size[x]
    else: 
      par[y]=par[x]
      size[x]+=size[y]
  else:
    return

for i in range(m):
  x,y,z=map(int,input().split())
  union(x-1,y-1)


ans={find(i) for i in range(n)}

print(len(ans))