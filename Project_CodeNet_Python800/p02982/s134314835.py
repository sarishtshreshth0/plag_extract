import math
N,D = map(int,input().split())
X = []
for i in range(N):
  X.append(list(map(int,input().split())))
ans = 0
for i in range(N):
  for j in range(i+1,N):
    now = 0
    dis = 0
    for k in range(D):
      now += (X[i][k]-X[j][k])**2
    dis = math.sqrt(now)
    if dis%1 == 0:
      ans += 1
print(ans)