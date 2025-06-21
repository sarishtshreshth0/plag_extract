from functools import reduce
n, a, b = map(int, input().split())
mod = 10**9 + 7

def f(A):
    bunsi = reduce(lambda x, y: x*y%mod, range(n, n-A, -1))
    bunbo = reduce(lambda x, y: x*y%mod, range(1, A+1))
    return bunsi * pow(bunbo, mod-2, mod) % mod

ans = pow(2, n, mod) - f(a) -f(b) - 1
ans %= mod
print(ans)