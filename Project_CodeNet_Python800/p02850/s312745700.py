import sys
sys.setrecursionlimit(500000)

N = int(input())

#道を双方向に記録する。
g = [[] for _ in range(N)]

for i in range(N-1): #木の辺の数はN-1
  #iが辺のID
  a,b = map(int,input().split())
  a -= 1; b -= 1 #ここで引いて頂点を0スタートにしないとオーバーフロー
  g[a].append((b,i))
  g[b].append((a,i))

#これが答え。
ans = [-1 for _ in range(N-1)]

#vという頂点からpという親にcolorという色で繋がっている。
def dfs(v, color, p):
  k = 1 #色の初期値
  for i in range(len(g[v])): #vから繋がっている頂点をtoとして探す
    TO = g[v][i][0]
    ID = g[v][i][1]
    if TO == p: #親は一つでそれ以外は子。親の時だけ無視すればよい。
      continue
    if k == color: #親から繋がっている色と被ったらダメ。
      k += 1
    ans[ID] = k
    k += 1 #ここで足す1をしないとこのfor loopの中の辺で色が被る。
    dfs(TO,ans[ID],v)

dfs(0,0,-1) #根を0として、仮想親の-1から仮想色0で繋がっている。
print(max(ans))
for i in ans:
  print(i)