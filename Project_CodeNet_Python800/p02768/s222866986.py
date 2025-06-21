import math
n, a, b = map(int, input().split())
mod = 10**9 + 7

ans = pow(2, n, mod) - 1

x = 1
y = 1
for i in range(a):
  x = x*(n - i)%mod
  y = y*(i + 1)%mod
ans -= x*pow(y, mod - 2, mod)%mod
  
x = 1
y = 1
for i in range(b):
  x = x*(n - i)%mod
  y = y*(i + 1)%mod
ans -= x*pow(y, mod - 2, mod)%mod
  
print(ans%mod)
