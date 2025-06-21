n, a, b = map(int, input().split())
mod = 10**9 + 7
 
def powerDX(n, r, mod):
  if r == 0: return 1
  if r%2 == 0:
    return pow(n*n % mod, r//2, mod) % mod
  if r%2 == 1:
    return n * pow(n, r-1, mod) % mod
 
def combination(n, r, mod=10**9+7):
    n1, r = n+1, min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod
 
ans = pow(2, n, mod) - 1
ans -=  combination(n, a, mod)
ans -=  combination(n, b, mod)
ans += 3*mod
ans %= mod
print(ans)