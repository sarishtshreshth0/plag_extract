n, a, b = map(int, input().split())
mod = 10**9+7
ans = pow(2, n, mod)-1

modp = mod                     # 素数であることが前提
max_r = 10 ** 7               # 必要分だけ用意する 10**7が限度
factinv = [1, 1] + [0]*max_r  # factinv[n] = ((n!)^(-1) mod modp)
inv = [0, 1] + [0]*max_r      # factinv 計算用

fact = {}

def cmb(n, r, p):
    assert n < p, 'n is less than modp'
    assert r < max_r, 'n in less than max_n'
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    if (n, r) in fact:
        return fact[(n, r)] * factinv[r] % p
    else:
        f = 1
        for i in range(n, n-r, -1):
            f = f * i % p
        fact[(n, r)] = f
        return f * factinv[r] % p

for i in range(2, max_r + 1):
    inv[i] = (-inv[modp % i] * (modp // i)) % modp
    factinv[i] = (factinv[i-1] * inv[i]) % modp

ans-=cmb(n, a, mod)
ans-=cmb(n, b, mod)
print(ans%mod)
