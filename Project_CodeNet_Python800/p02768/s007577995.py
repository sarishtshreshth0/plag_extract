def resolve():
    n, a, b = list(map(int, input().split()))
    MOD = 10**9+7
    ntoa = 1
    ato1 = 1
    ntob = 1
    bto1 = 1
    for i in range(a):
        ntoa *= (n-i)
        ntoa %= MOD
        ato1 *= (a-i)
        ato1 %= MOD
    for i in range(b):
        ntob *= (n-i)
        ntob %= MOD
        bto1 *= (b-i)
        bto1 %= MOD
    def pow(x, n, MOD=10**9+7):
        ret = 1
        while n > 0:
            if n & 1:
                ret = (ret*x)%MOD
            x = (x*x)%MOD
            n >>= 1
        return ret
    nca = ntoa*pow(ato1, MOD-2)%MOD
    ncb = ntob*pow(bto1, MOD-2)%MOD
    print((pow(2, n)%MOD-1-nca-ncb)%MOD)

if '__main__' == __name__:
    resolve()
