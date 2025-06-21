def combination_mod(n, r, mod):
    x = 1
    y = 1

    for i in range(r):
        x *= n - i
        y *= r - i
        x %= mod
        y %= mod

    return (x * pow(y, mod - 2, mod)) % mod


n, a, b = map(int, input().split())
mod = 10 ** 9 + 7


ans = pow(2, n, mod) - 1
ans %= mod
ans -= combination_mod(n, a, mod)
ans %= mod
ans -= combination_mod(n, b, mod)
ans %= mod

print(ans)

