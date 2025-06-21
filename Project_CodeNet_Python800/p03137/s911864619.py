N, M = map(int,input().split())
X = list(map(int,input().split()))

if N >= M:
  print(0)
else:
  X.sort()
  dist = []
  
  for i in range(M-1):
    dist.append(X[i+1] - X[i])
    
  dist.sort()
  ans = 0
  
  for i in range(M-N):
    ans += dist[i]
    
  print(ans)