n, a, b = list(map(int, input().split()))
MOD = 10**9 + 7

# 1!からmax(a, b)!までの逆元をMODで割ったあまりと
# nからn-max(a*b)までをかけてMODで割ったあまりを求めます。
fact = {}
fact[n] = n
fact[n - 1] = fact[n] * (n - 1) % MOD

inv_fact = [0] * (max(a, b) + 1)
inv_fact[1] = 1

for i in range(2, max(a, b) + 1):
    fact[n - i] = fact[n - i + 1] * (n - i) % MOD
    inv_fact[i] = inv_fact[i - 1] * pow(i, -1, MOD) % MOD

subtrahend = 1 + fact[n - a + 1] * inv_fact[a] + fact[n - b + 1] * inv_fact[b]
minuend = pow(2, n, MOD)

print((minuend + 2 * MOD - subtrahend) % MOD)
