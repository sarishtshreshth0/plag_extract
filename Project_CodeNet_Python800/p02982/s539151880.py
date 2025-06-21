N, D = map(int, input().split())
X = []
for n in range(N):
  X.append(list(map(int, input().split())))

def check_dist(i, j):
  quad = sum([(xi - xj) * (xi - xj) for xi,xj in zip(X[i], X[j])])
  dist = 1
  while dist * dist <= quad:
    if dist * dist == quad:
      return True
    dist += 1
  return False

count = 0
for i in range(N-1):
  for j in range(i+1, N):
    count += check_dist(i, j)
print(count)