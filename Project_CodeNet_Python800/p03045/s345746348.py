N,M=map(int,input().split())  
par=[i for i in range(N)]
rank=[0]*(N)
def find(x):
  if par[x]==x:
    return x
  else:
    par[x]=find(par[x])
    return par[x]

def same(x,y):
  return find(x)==find(y)

def union(x,y):
  x=find(x)
  y=find(y)
  if x==y:
    return 
  if rank[x]>rank[y]:
    par[y]=x
  else:
    par[x]=y
    if rank[x]==rank[y]:
      rank[y]+=1

for i in range(M):
  a,b,c=map(int,input().split())
  a-=1
  b-=1
  union(a,b)

cnt=0
for i in range(N):
  if i==par[i]:
    cnt+=1
print(cnt)