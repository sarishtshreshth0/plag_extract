MOD = 10 ** 9 + 7

def nCk(n, k):
    if k > n or min(n, k) < 0:
        raise Exception('Not correct input values!')
    res = 1
    for i in range(1, k + 1):
        res = (res * (n - i + 1) * pow(i, MOD - 2, MOD)) % MOD
    return res

n, a, b = map(int, input().split())
ret = (pow(2, n, MOD) - 1 - nCk(n, a) - nCk(n, b)) % MOD
print(ret)