N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))

if N >= M:
  print(0)
else:
  L = sorted([X[i + 1] - X[i] for i in range(M - 1)], reverse=True)
  print(X[-1] - X[0] - sum([L[i] for i in range(N - 1)]))