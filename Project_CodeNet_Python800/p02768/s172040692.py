def modpow(a, n, p):
    if n == 0: return 0
    elif n == 1: return a % p
    elif n % 2: return (a * modpow(a, n - 1, p)) % p
    else:
        t = modpow(a, n // 2, p)
        return (t * t) % p

def calc(n, r):
    p, q = 1, 1
    for i in range(r):
        p = p * (n - i) % MOD
        q = q * (i + 1) % MOD
    return p * modpow(q, MOD - 2, MOD) % MOD
    

MOD = 10 ** 9 + 7

N, a, b = map(int, input().split())
s = modpow(2, N, MOD) - 1
print((s - (calc(N, a) + calc(N, b))) % MOD)
