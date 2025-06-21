N, M = map(int, input().split())
par = [i for i in range(N)]
rank = [0 for i in range(N)]
def root(x):
  if par[x] == x:
    return x
  else:
    par[x] = root(par[x])
    return par[x]
def unite(x, y):
  x, y = root(x), root(y)
  if x != y:
    if rank[x] < rank[y]:
      par[x] = y
    else:
      par[y] = x
      if rank[x] == rank[y]:
        rank[x] += 1

for i in range(M):
  X, Y, Z = map(int, input().split())
  unite(X-1, Y-1)
for i in range(N):
  root(i)
print(len(set(par)))