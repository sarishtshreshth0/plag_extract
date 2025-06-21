n, a, b = map(int, input().split())

M = 10 ** 9 + 7

all = pow(2, n, M) - 1
all %= M

def C(n,x):
    num = 1
    den = 1
    for i in range(x):
        num *= (n-i)
        num %= M
        den *= (i+1)
        den %= M

    inv = pow(den, M-2, M)

    return num * inv % M

ans = all - C(n,a) - C(n,b)
ans %= M
print(ans)