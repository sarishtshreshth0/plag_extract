import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
adj = [ [] for _ in range(N) ]
for i in range(N-1):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  adj[a].append((b,i))

res = [None] * (N-1)
def dfs(n, c=-1, p=-1):
  if c==-1 or c>1: 
    nc = 1
  else:
    nc = c+1
  for nei,i in adj[n]:
    if nei == p: continue
    res[i] = nc
    dfs(nei, nc, n)
    nc += 1
    if nc==c: nc += 1

dfs(0)
print(max(res))
for r in res: print(r)