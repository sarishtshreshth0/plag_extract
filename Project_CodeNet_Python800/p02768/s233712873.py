n, a, b = map(int, input().split())

mod = 10 ** 9 + 7

def frac_rev(n, r):
  x = 1
  for i in range(n, n-r, -1):
    x = x * i % mod
  return x

def frac(n):
  x = 1
  for i in range(1, n+1):
    x = x * i % mod
  return x

print(( pow(2, n, mod) - 1 - frac_rev(n, a) * pow(frac(a), mod-2, mod) % mod - frac_rev(n, b) * pow(frac(b), mod-2, mod) % mod) % mod)