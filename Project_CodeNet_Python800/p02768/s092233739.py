def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)


# return nCk % mod
# it takes O(k)
def mod_comb(n, k, mod):
    numer, denom = 1, 1
    for i in range(k):
        numer = numer * ((n - i) % mod) % mod
        denom = denom * ((i + 1) % mod) % mod

    return numer * mod_inverse(denom, mod) % mod


mod = 10**9 + 7
n, a, b = map(int, input().split())

ans = pow(2, n, mod) - 1
ans = (ans - mod_comb(n, a, mod)) % mod
ans = (ans - mod_comb(n, b, mod)) % mod
ans = (ans + mod) % mod

print(ans)