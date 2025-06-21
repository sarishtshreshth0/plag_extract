import sys
sys.setrecursionlimit(10 ** 9)
#島ごとに　島の人口ー友達の数ーブロックの数ー自分一人＝友達候補の数
N,M,K = map(int,input().split())
G = [[] for i in range(N+1)]
for i in range(M):
  a,b = map(int,input().split())
  G[a].append(b)
  G[b].append(a)
bl = [[] for i in range(N+1)]  
for i in range(K):  
  c,d = map(int,input().split())
  bl[c].append(d)
  bl[d].append(c)

seen = [False for i in range(N+1)]  
lcnt = [1]
lmen = []
def dfs(p):
  for v in G[p]:
    if seen[v] == False:
      seen[v] = True
      lmen.append(v)
      lcnt[0] += 1
      dfs(v)

#unionfind
lp = [i for i in range(N+1)] #親のリスト
#木の根を求める
def root(x):
  if lp[x] == x:
    return x
  else:
    lp[x] = root(lp[x])
    return lp[x]
#xとyが同じ集合に属するか否か
def det(x,y):
  return root(x) == root(y)
#xとYが属する集合の併合 Yが親になる
def unite(x,y):
  x = root(x)
  y = root(y)
  if x != y:
    lp[x] = y      

popu = [0 for i in range(N+1)] 
bpopu = [0 for i in range(N+1)]
seen = [False for i in range(N+1)] 
for i in range(1,N+1):
  if seen[i] == False:
    seen[i] = True

    lcnt = [1]
    lmen = [i]
    dfs(i)
    #根iに人口を記載
    popu[i]=lcnt[0]
    for j in lmen:
      unite(j,i)
    for j in lmen:  
      c = 0
      for k in bl[j]:
        if det(k,i):
          c += 1
      bpopu[j] = c
###
for i in range(1,N+1):
  print( popu[root(i)]-len(G[i])-bpopu[i]-1 )