import math

def is_int(n):
  return True if int(n) == n else False

def dist(x, y):
  buf = 0
  for i in range(len(x)):
    buf += (x[i] - y[i]) ** 2
  return math.sqrt(buf)
    

N, D = list(map(lambda a: int(a), input().split(" ")))
X = []
for i in range(N):
  X.append(list(map(lambda x: int(x), input().split(" "))))

cnt = 0

for j in range(N):
  for k in range(j):
    if is_int(dist(X[j], X[k])):
      cnt += 1

print(cnt)
