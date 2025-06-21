n, a, b = map(int, input().split())
mod = pow(10, 9) + 7


def cmb(n,r):
    mod = 10**9+7
    ans = 1
    for i in range(r):
        ans *= n-i
        ans %= mod
    for i in range(1,r+1):
        ans *= pow(i,mod-2,mod)
        ans %= mod
    return ans


total = pow(2, n, mod) - cmb(n, a) - cmb(n, b) - 1
print(total % mod)