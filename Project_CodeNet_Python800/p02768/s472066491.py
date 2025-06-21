n, a, b = map(int, input().split())

lm = min(n, 2*10**5)

# ①nCrの各項のmod(10^9+7)を事前計算
p = 10 ** 9 + 7
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, lm + 1):
  fact.append((fact[-1] * i) % p)
  inv.append((-inv[p % i] * (p // i)) % p)
  factinv.append((factinv[-1] * inv[-1]) % p)

# ②事前計算した項を掛け合わせ
def cmb(n, r, p):
  if (r < 0) or (n < r):
    return 0
  r = min(r, n - r)
  rt = 1
  for i in range(r):
    rt = (rt * (n-i)) % p
  rt = rt*factinv[r] % p
  return rt

def pow_r(x, n, p):
  """
  O(log n)
  """
  if n == 0:  # exit case
    return 1
  if n % 2 == 0:  # standard case ① n is even
    return pow_r(x ** 2 % p, n // 2, p)
  else:  # standard case ② n is odd
    return x * pow_r(x ** 2 % p, (n - 1) // 2, p) % p

rlt = pow_r(2,n,p)
  
rlt -= 1


rlt -= cmb(n,a,p) % p
rlt -= cmb(n,b,p) % p

while rlt < 0:
  rlt += p

print(rlt)