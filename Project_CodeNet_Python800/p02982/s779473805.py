import math
N, D = map(int, input().split())
X = []
for i in range(N):
  x = list(map(int, input().split()))
  X.append(x)
  
ans = 0
for i in range(N-1):
  for j in range(i+1, N):
    total = 0
    for k in range(D):
      total += (X[i][k] - X[j][k]) ** 2
    if math.sqrt(total).is_integer():
      ans += 1
      
print(ans)