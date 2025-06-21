from math import gcd
N, X = map(int, input().split())
L = list(map(lambda x: abs(int(x) - X), input().split()))
L.sort()
if N == 1:
  print(L[0])
elif N == 2:
  print(gcd(L[0], L[1]))
else:
  ans = gcd(L[0], L[1])
  for l in L[2:]:
    ans = gcd(ans, l)
  print(ans)