from collections import deque

N = int(input())

g = [[] for _ in range(N)]
hen = []
dic = {}
for i in range(N-1):
  #iが辺のID
  a,b = map(int,input().split())
  a -= 1; b -= 1
  g[a].append((b,i))
  g[b].append((a,i))

#これが答え。辺の本数だけ空を用意する。
ans = [0 for _ in range(N-1)]

Q = deque([])
Q.append(0)
used = [0 for _ in range(N)] #訪れた頂点をここに記録
used[0] = 1
#pre = [-1 for _ in range(N)]

while Q:
  v = Q.popleft()
  #p = pre[v] #vの親
  c = -1
  for i in range(len(g[v])): #vとvの親が繋がっている色を探す。
    TO = g[v][i][0]
    ID = g[v][i][1]
    if used[TO] == 1:
      c = ans[ID]
  k = 1
  for i in range(len(g[v])): #vとつながっている親以外の色を塗っていく。
    TO = g[v][i][0]
    ID = g[v][i][1]
    if used[TO] == 1:
      continue
    if k == c:
      k += 1
    ans[ID] = k
    k += 1
    Q.append(TO)
    used[TO] = 1
    


#bfs(0,0,-1) #根を0として、仮想親の-1から仮想色0で繋がっている。
print(max(ans))
for i in ans:
  print(i)