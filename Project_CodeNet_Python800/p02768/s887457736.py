
n, a, b = map(int, input().split())
mod = 10 ** 9 + 7

ans = pow(2, n, mod) - 1

nca, ncb = 1, 1

for i in range(b):
    ncb = ncb * (n - i) % mod
    ncb *= pow(i + 1, mod - 2, mod)
    if i + 1 == a:
        nca = ncb

print((ans - (nca + ncb)) % mod)