def modComb(n,r,mod):
    nume = 1
    deno = 1
    for i in range(r):
        nume = nume*(n-i) % mod
        deno = deno*(i+1) % mod
    return nume*pow(deno, mod-2, mod) % mod

n, a, b = map(int, input().split())

mod = 10**9+7

ans = (pow(2, n, mod) -1 -modComb(n,a,mod) - modComb(n,b,mod)) % mod

print(ans)