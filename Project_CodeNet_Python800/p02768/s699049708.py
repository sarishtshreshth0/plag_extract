n, a, b = map(int, input().split())

mod = 1000000007

def pow(x, n):
    ret = 1
    while n > 0:
        if (n & 1) == 1:
            ret = (ret * x) % mod
        x = (x * x) % mod
        n //= 2
    return ret

def inv(x):
    return pow(x, mod - 2)

def cmb(n, k):
    ret = 1
    for i in range(k):
        ret = (ret * (n - i) * inv(i + 1)) % mod
    return ret

print((pow(2, n) - cmb(n, a) - cmb(n, b) - 1) % mod)
