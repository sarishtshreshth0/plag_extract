N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
if N >= M:
  print(0)
else:
  Y = []
  for i in range(M-1):
    Y.append(X[i+1] - X[i])
  Y.sort(reverse=True)
  print(X[-1] - X[0] - sum(Y[:N-1]))