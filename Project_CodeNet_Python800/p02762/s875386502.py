import sys
sys.setrecursionlimit(10 ** 9)

n, m, k = map(int, input().split())
ab = [[] for i in range(n)]

for i in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  ab[a].append(b)
  ab[b].append(a)

block = [set() for i in range(n)]
for i in range(k):
  c, d = map(int, input().split())
  c -= 1
  d -= 1
  block[c].add(d)
  block[d].add(c)

ans = [0 for i in range(n)]

def dfs(s):
  if vis[s] == False:
    vis[s] = True
    r[cnt].add(s)
    for i in ab[s]:
      dfs(i)

vis = [False for i in range(n)]
r = []
cnt = 0
for i in range(n):
  if vis[i] == False:
    r.append(set())
    dfs(i)
    cnt += 1

ans = [0 for i in range(n)]
for i in r:
  l = len(i)
  for j in i:
    ans[j] = l - len(ab[j]) - len(i&block[j]) - 1

print (*ans)