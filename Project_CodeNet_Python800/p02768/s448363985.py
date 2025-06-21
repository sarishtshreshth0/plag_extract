import math
n, a, b = map(int, input().split())
p = 10 ** 9 + 7
#ans = 2 ** n - 1 - N C a - N C b

def modpow(a, n, MOD):
  res = 1
  while (n > 0):
    if (n & 1):
      res = res * a % MOD
    a = a * a % MOD
    n >>= 1
  return res

def cmb(n, r, p):
  A = 1
  for i in range(r):
    A *= (n - i)
    A *= modpow(i + 1, p - 2, p)
    A %= p
  return A

ans = (modpow(2, n, p) - 1) % p
ans -= cmb(n, a, p) + cmb(n, b, p)

print(ans % p)





