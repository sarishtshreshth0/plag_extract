n, a, b = map(int, input().split())
mod = 10**9+7
ans = pow(2, n, mod)-1

nCa = 1
nCb = 1
for i in range(b):
    nCb *= (n-i)
    nCb %= mod
    nCb *= pow(i+1, mod-2, mod)
    if i == a-1:
        nCa = nCb
ans -= nCa
ans %= mod
ans -= nCb
ans %= mod

print(ans)