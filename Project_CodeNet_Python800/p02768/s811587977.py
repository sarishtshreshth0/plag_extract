n, a, b = map(int, input().split())
mod = 10**9+7

def mypow(x, y, mod):
   ans = 1
   while y > 0:
      if bin(y & 1) == bin(1):
         ans *= x % mod
      x *= x % mod
      y = y >> 1
   return ans

def comb(n, r, mod):
   num, denom = 1, 1
   for i in range(1, r+1):
      num = (num*(n+1-i)) % mod
      denom = (denom*i) % mod
   return num * mypow(denom, mod-2, mod) % mod

print((mypow(2, n, mod) - 1 - comb(n, a, mod) - comb(n, b, mod)) % mod)
