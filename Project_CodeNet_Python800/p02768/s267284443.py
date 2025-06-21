n, a, b = map(int, input().split())

mod = 10 ** 9 + 7

ans = pow(2, n, mod) - 1
for i in [a, b]:
    num = 1
    den = 1
    for p in range(n, n-i, -1):
        num = num * p % mod
    for q in range(1, i+1):
        den = den * q % mod
    cmb = num * pow(den, mod-2, mod) % mod
    ans -= cmb
    ans %= mod
print(ans)