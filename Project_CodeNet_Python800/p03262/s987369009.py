from math import gcd
N, X = map(int, input().split())
A = list(map(lambda x: abs(int(x) - X), input().split()))
g = A[0]
for i in range(1, N):
  g = gcd(g, A[i])
print(g)