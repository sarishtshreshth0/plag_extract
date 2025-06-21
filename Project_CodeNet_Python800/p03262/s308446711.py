from math import gcd
N,X = map(int, input().split())
L = list(map(int, input().split()))
k = 0
for i in L:
  if k == 0:
    k = i - X
  else:
    k = gcd(k, i-X)
print(abs(k))