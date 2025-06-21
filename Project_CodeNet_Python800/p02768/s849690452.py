def inverse(a, mod):
    a %= mod
    p = mod
    x, y = 0, 1
    while a > 0:
        n = p // a
        p, a = a, p % a, 
        x, y = y, x - n * y
    return x % mod

def power(x, n, mod):
    ans = 1
    while n > 0:
        if n % 2 == 1:
            ans = ans * x % mod
        n //= 2
        x = x * x % mod
    return ans

n, a, b = map(int, input().split())
mod = 10 ** 9 + 7
ans = power(2, n, mod)
nCa = 1
for i in range(a):
    nCa = nCa * inverse(i + 1, mod) % mod * (n - i) % mod
nCb = 1
for i in range(b):
    nCb = nCb * inverse(i + 1, mod) % mod * (n - i) % mod
ans = (ans - nCa - nCb - 1) % mod
print(ans)