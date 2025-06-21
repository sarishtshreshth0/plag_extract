mod = 10**9+7

n, a, b = map(int, input().split())

def comb(n, r):
    c = 1
    for i in range(r):
        c *= n-i
        c %= mod

    d = 1
    for i in range(1, r+1):
        d *= i
        d %= mod

    return (c * pow(d, mod-2, mod)) % mod

ans = pow(2, n, mod) - 1 - comb(n, a) - comb(n, b)

ans %= mod

print(ans)

