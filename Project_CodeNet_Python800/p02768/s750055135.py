# AtCoder Beginner Contest 156
# D - Bouquet
# https://atcoder.jp/contests/abc156/tasks/abc156_d
n, a, b = map(int, input().split())
mod = 10**9 + 7

MAX = 202020

cmb = [0]*MAX
facinv = [0]*MAX
inv = [0]*MAX


def nCk_init(n, mod, MAX):
    facinv[0] = facinv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        inv[i] = -inv[mod % i] * (mod // i) % mod
        facinv[i] = facinv[i-1] * inv[i] % mod
    cmb[0] = 1
    for i in range(1, MAX):
        cmb[i] = cmb[i-1] * ((n-i+1)*inv[i] % mod) % mod


nCk_init(n, mod, MAX)
ans = pow(2, n, mod)
ans += mod - cmb[a]
ans %= mod
ans += mod - cmb[b]
ans %= mod
ans += mod - 1
ans %= mod
print(ans)
