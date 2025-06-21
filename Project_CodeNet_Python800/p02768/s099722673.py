def combination(n, r, m):
    res = 1
    r = min(r, n - r)

    for i in range(r):
        res = res * (n - i) % m
        res = res * pow(i + 1, m - 2, m) % m
    return res

mod = 10**9 + 7
n, a, b = map(int, input().split())
total = pow(2, n, mod) - 1

total -= (combination(n, a, mod) + combination(n, b, mod)) % mod

print(total % mod)