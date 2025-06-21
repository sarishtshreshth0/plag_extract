import math
N, D = map(int,input().split())
X = []
for i in range(N):
  tmp = list(map(int, input().split()))
  X.append(tmp)

count = 0
for i in range(N-1):
  for j in range(i+1, N):
    dst = 0
    for k in range(D):
      dst += (X[i][k]-X[j][k])**2
    dst = math.sqrt(dst)
    if dst == int(dst):
      count+=1
print(count)