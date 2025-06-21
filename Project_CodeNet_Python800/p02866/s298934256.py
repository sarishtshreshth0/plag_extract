def my_pow(base, n, mod):
    if n == 0:
        return 1
    x = base
    y = 1
    while n > 1:
        if n % 2 == 0:
            x *= x
            n //= 2
        else:
            y *= x
            n -= 1
        x %= mod
        y %= mod
    return x * y % mod

N = int(input())
D = list(map(int, input().split()))
dmax = max(D)
MOD = 998244353
cnt = [0] * (10 ** 5 + 1)
for d in D:
    cnt[d] += 1

if D[0] or cnt[0] != 1:
    print(0)
    exit()
ans = cnt[0]
for i in range(1, dmax + 1):
    now = my_pow(cnt[i - 1], cnt[i], MOD)
    ans *= now
    ans %= MOD
print(ans)