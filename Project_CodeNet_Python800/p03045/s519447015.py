import sys
sys.setrecursionlimit(500000) #これがないと再帰の回数オーバーでエラー出る。

N,M = map(int,input().split())

A = [[] for _ in range(N)]
for i in range(M):
  a,b,c = map(int,input().split())
  a -=1; b-=1
  A[a].append(b)
  A[b].append(a)
#print(A)

reach = [-1 for _ in range(N)] #-1が未到達、1が到達
def dfs(v):
  if reach[v] != -1:
    return
  else:
    reach[v] = 1
  for u in A[v]:
    dfs(u)
    
test = 0    
for i in range(N):
  if reach[i] == -1:
    dfs(i)
    test += 1
print(test)