from math import sqrt
N, D = map(int, input().split())
A = []
ans = 0
for i in range(N):
  A.append(list(map(int, input().split())))
for i in range(N-1):
  for j in range(i+1, N):
    d = 0
    for k in range(D):
      d += (A[i][k] - A[j][k]) ** 2
    if int(sqrt(d)) ** 2 == d:
      ans += 1
print(ans)