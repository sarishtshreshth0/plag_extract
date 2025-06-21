n, a, b = map(int, input().split())
mod = 10**9+7
ans = pow(2, n, mod) - 1

up = 1
bo = 1
for i in range(b):
    up = up*(n-i)%mod
    bo = bo*(i+1)%mod
    if i == a-1:
        acombs = up*pow(bo, mod-2, mod)%mod

bcombs = up*pow(bo, mod-2, mod)%mod

print((ans - acombs - bcombs)%mod)
