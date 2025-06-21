N,M = map(int,input().split())
X = list(map(int,input().split()))

ans = 0

if N >= M:
  pass
else:
  X.sort()
  dist = []

  for i in range(1,M):
    dist.append(abs(X[i]-X[i-1]))
  dist = sorted(dist, reverse= True)

  ans = sum(dist[N-1:])

print(ans)