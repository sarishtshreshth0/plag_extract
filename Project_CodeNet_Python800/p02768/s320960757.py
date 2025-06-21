n, a, b = map(int, input().split())

mod = 10 ** 9 + 7
N = min(n, 2 * 10**5)
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]

def comb(n, r):
  return fac[n] * ( finv[r] * finv[n-r] % mod ) % mod
 
for i in range(2, N + 1):
  fac.append( ( fac[-1] * i ) % mod )
  inv.append( mod - ( inv[mod % i] * (mod // i) % mod ) )
  finv.append( finv[-1] * inv[-1]  % mod )

def frac_rev(n, r):
  x = 1
  for i in range(n, n-r, -1):
    x = x * i % mod
  return x

if n <= 2 * 10**5:
  print(( pow(2, n, mod) - 1 - comb(n, a) -comb(n, b) ) % mod)
else:
  print(( pow(2, n, mod) - 1 - frac_rev(n, a) * finv[a] % mod - frac_rev(n, b) * finv[b] % mod) % mod)