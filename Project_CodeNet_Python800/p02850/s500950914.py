# ある頂点で、子供に対して順に1,2,3...と辺の色を渡していく
# 親から来た色を持っておき、親から来た色と同色になったときはスキップして次の色を渡す
# グラフ構築の際に、辺の番号を持っておく

import sys
readline = sys.stdin.readline

N = int(readline())
G = [[] for i in range(N)]
for i in range(N - 1):
  a,b = map(int,readline().split())
  G[a-1].append([b-1,i])
  G[b-1].append([a-1,i])
  
ans = [0 for i in range(N - 1)]
from collections import deque
# 頂点、親から来た色、親
q = deque([[0, 0, -1]])
while q:
  v,pcol,parent = q.popleft()
  cnt = 1
  for child in G[v]:
    if child[0] == parent:
      continue
    if cnt == pcol:
      cnt += 1
    ans[child[1]] = cnt
    q.append([child[0],cnt,v])
    cnt += 1

print(max(ans))
for a in ans:
  print(a)