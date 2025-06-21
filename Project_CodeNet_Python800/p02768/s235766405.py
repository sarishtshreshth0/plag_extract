n, a, b = list(map(int, input().split()))
p = 10**9+7

def binom(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)

    res = factinv[r] % p
    for i in range(r):
        res = res * (n - i) % p

    return res % p

factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, min(n, 2*10**5) + 1):
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

res = pow(2, n, p)

res -= 1
res = (res - binom(n, a, p)) % p
res = (res - binom(n, b, p)) % p

print(res)