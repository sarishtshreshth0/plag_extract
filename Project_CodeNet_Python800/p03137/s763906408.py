N, M = map(int, input().split())
X = sorted(map(int, input().split()))

dis = [0]*(M-1)

for i in range(M-1):
  dis[i] = X[i+1] - X[i]

dis.sort()

if N < M:
  print(sum(dis[:M-N]))
else:
  print(0)