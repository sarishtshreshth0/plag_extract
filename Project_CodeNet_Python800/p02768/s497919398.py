def inverse(n, mod):
    return pow(n, mod - 2, mod)

def cmb(n, r, mod):
    p, q = 1, 1
    for i in range(r):
        p = p * (n - i) % mod
        q = q * (i + 1) % mod
    return p * inverse(q, mod) % mod

n, a, b = map(int, input().split())
mod = 10 ** 9 + 7
ans = pow(2, n, mod) - 1
ans -= cmb(n, a, mod)
ans -= cmb(n, b, mod)
print(ans % mod)
