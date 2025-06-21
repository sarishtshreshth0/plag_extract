n,a,b = map(int, input().split())
MOD = 10**9 + 7
allpair = pow(2,n,MOD)

def combo(n,k):
    c = 1
    for i in range(k):
        c *= n - i
        c %= MOD

    d = 1
    for i in range(1, k+1):
        d *= i
        d %= MOD

    return (c * pow(d, MOD-2, MOD)) % MOD

print((allpair - combo(n, a) - combo(n, b) - 1) % MOD)
