from fractions import gcd
N, X = map(int, input().split())
A = list(map(int, input().split()))
g = 0
for i in range(N):
  if i == 0:
    g = gcd(g, abs(X - A[0]))
  else:
    g = gcd(g, abs(A[i] - A[i-1]))
print(g)