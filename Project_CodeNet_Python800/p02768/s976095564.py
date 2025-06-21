import copy

def fast_pow(x, n, MOD):
    res = 1
    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1
    return res
  
  
def prepare(n, MOD):
 
    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
     
    return factorials, invs

MOD = 10**9+7
fact, fact_inv = prepare(2*10**5, MOD)

n, a, b = map(int,input().split())
f = copy.deepcopy(n)
for i in range(1, b+1):
    if i == a:
        nca = f * fact_inv[a] % MOD
    if i == b:
        ncb = f * fact_inv[b] % MOD
        break
    f = f * (n - i) % MOD
print((fast_pow(2, n, MOD) - 1 - nca - ncb) % MOD)

