def abp(a, b, p):
    if b == 0:
        return 1
    if b % 2 == 0:
        tmp = abp(a, b // 2, p)
        return (tmp * tmp) % p
    if b % 2 == 1:
        return (a * abp(a, b - 1, p)) % p

def nCr(n, r, p):
    total = 1
    for i in range(r):
        total *= (n - i) * abp(r - i, p - 2, p)
        total %= p
    return total

n, a, b = map(int, input().split())
p = 1000000007
ret = abp(2, n, p) - nCr(n, a, p) - nCr(n, b, p) - 1
print(ret % p)
