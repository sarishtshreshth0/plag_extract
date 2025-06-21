from functools import reduce
N,a,b = map(int,input().split())
MOD = 10**9+7
def f(r):
    nPr = reduce(lambda x,y: x * y % MOD,range(N,N-r,-1))
    r_fact = reduce(lambda x,y: x * y % MOD,range(1,r+1))
    return nPr * pow(r_fact,MOD-2,MOD) % MOD
result = pow(2,N,MOD) - f(a) - f(b) - 1
result %= MOD
print(result)
