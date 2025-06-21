import sys
sys.setrecursionlimit(1000000)
def II(): return int(input())
def MI(): return map(int, input().split())
N=II()
edge=[[] for i in range(N)]
a=[0]*N
b=[0]*N
for i in range(N-1):
  a[i],b[i]=MI()
  a[i]-=1
  b[i]-=1
  edge[a[i]].append(b[i])
  edge[b[i]].append(a[i])
k=0
color_dict={}
def dfs(to,fm=-1,ban_color=-1):
  global k
  color=1
  for nxt in edge[to]:
    if nxt==fm:
      continue
    if color==ban_color:
      color+=1
    color_dict[(to,nxt)]=color
    dfs(nxt,to,color)
    color+=1
  k=max(k,color-1)
dfs(0)
print(k)
for i in range(N-1):
  print(color_dict[(a[i],b[i])])