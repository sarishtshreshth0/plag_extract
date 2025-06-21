MOD = pow(10, 9) + 7

def modinv(a, mod):
    return pow(a, mod - 2, mod) % mod

def comb(n, r, mod):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) % mod
        res = res * modinv(i + 1, mod) % mod
    return res

n, a, b = map(int, input().split())

ans = (pow(2, n, MOD) - 1 - comb(n, a, MOD) - comb(n, b, MOD)) % MOD

print(ans)
