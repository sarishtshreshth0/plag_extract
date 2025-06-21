n, a, b = map(int, input().split())
mod = 10**9 + 7

ans = pow(2, n, mod) - 1

def comb(m):
    x = 1
    y = 1
    for i in range(m):
        x = x*(n - i)%mod
        y = y*(i + 1)%mod
    return (x*pow(y, mod - 2, mod)%mod)

print((ans - comb(a) - comb(b))%mod)