N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
c = 0
for i in range(N):
  for j in range(i+1, N):
    c += (sum((X[i][p]-X[j][p])**2 for p in range(D))**.5).is_integer()
print(c)