def modpow(x, n, m):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = (res * x) % m
        x = (x * x) % m
        n >>= 1
    return res

def combination(n, r, m):
    res = 1
    r = min(r, n - r)

    for i in range(1, r + 1):
        res = res * (n - r + i) % m
        res = res * modpow(i, m - 2, m) % m
    return res

mod = 10**9 + 7
n, a, b = map(int, input().split())
total = modpow(2, n, mod) - 1

total = (total - combination(n, a, mod) - combination(n, b, mod)) % mod

print(total)