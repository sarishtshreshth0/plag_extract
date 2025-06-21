N, D = map(int, input().split())

X = [list(map(int, input().split())) for i in range(N)]

sq = set()
for i in range(1, 1000):
  sq.add(i**2)

def foo(x,y):
  t = 0
  for i, j in zip(X[x], X[y]):
    t += (i - j) * (i - j)
  if t in sq:
    return 1
  else:
    return 0
    
ans = 0

for i in range(N):
  for j in range(i+1, N):
    ans += foo(i, j)

print(ans)
