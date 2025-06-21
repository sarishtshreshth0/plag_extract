n,a,b = map(int, input().split())
MOD = 10 ** 9 + 7

def comb(n, k):
    nCk = 1


    for i in range(n - k + 1, n + 1):
        nCk *= i
        nCk %= MOD

    for i in range(1, k + 1):
        nCk *= pow(i, MOD - 2, MOD)
        nCk %= MOD
    return nCk

print((((pow(2,n,MOD)-1-comb(n,a))%MOD)-comb(n,b))%MOD)