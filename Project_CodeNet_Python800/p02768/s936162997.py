n, a, b = map(int, input().split())
MOD = 10**9 + 7

u = [1]
d = [1]
c = [1]
for i in range(1, b+1):
    u.append(u[-1] * (n-i+1) % MOD)
    d.append(d[-1] * i % MOD)
    # c.append(u[-1] // d[-1] % MOD)
    c.append(u[-1] * pow(d[-1], MOD-2, MOD) % MOD)

print((pow(2, n, MOD) - c[a] - c[b] - 1) % MOD)