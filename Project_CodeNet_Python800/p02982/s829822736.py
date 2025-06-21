import math
N, D = map(int, input().split())
v = []
for i in range(N):
  temp =  list(map(int, input().split()))
  v.append(temp)
res = 0
for i in range(N-1):
  for j in range(i+1, N):
    temp = 0
    for k in range(D):
      temp += (v[i][k] - v[j][k]) ** 2
    temp = math.sqrt(temp)
    if temp.is_integer():
      res += 1
print(res)