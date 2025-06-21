import math
N, D = map(int, input().split())
a = []
ans = 0
for _ in range(N):
  tmp = list(map(int, input().split()))
  a.append(tmp)
for n in range(N):
  for m in range(n+1,N):
    dis = 0
    for d in range(D):
      dis += (a[n][d]-a[m][d])**2
    if math.sqrt(dis) == int(math.sqrt(dis)):
      ans += 1
print(ans)

