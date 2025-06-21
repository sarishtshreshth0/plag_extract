n, a, b = map(int, input().split())
mod = 10**9+7
ans = pow(2, n, mod)-1

def comb(n, a, mod):
    ans = 0
    u = 1
    for i in range(a):
        u *= n-i
        u %= mod
    d = 1
    for i in range(a):
        d *= i+1
        d %= mod
    ans = u*pow(d, mod-2, mod) % mod
    return ans
ans -= comb(n, a, mod)
ans -= comb(n, b, mod)
ans %= mod

print(ans)