n,m,k=map(int,input().split())

par=[i for i in range(n)]
size=[1 for i in range(n)]


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

graph=[[] for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    union(a-1,b-1)
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(k):
    a,b=map(int,input().split())
    if find(a-1)==find(b-1):
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

ans=[]

for i in range(n):
    cnt=size[find(i)]
    xxx=list(set(graph[i]))
    cnt-=len(xxx)
    cnt-=1
    ans+=[str(cnt)]


print(' '.join(ans))