import math
n, a, b = map(int, input().split())
mod = 10**9 + 7
s = pow(2, n, mod) - 1
def cal(n, r):
  p = 1
  q = 1
  for i in range(r):
    p = p*(n-i)%mod
    q = q*(i+1)%mod
  return p*pow(q, mod-2, mod)%mod
print((s - cal(n, a) - cal(n, b))%mod)