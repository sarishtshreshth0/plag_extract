n,a,b = map(int,input().split())
mod = 10**9+7

def modInverse(a,p):
    # Fermat's little theorem, a**(p-1) = 1 mod p
    return pow(a,p-2,p)

def nCr(n,r,p=mod):
    num = 1
    den = 1
    for i in range(r):
        num = (num*(n-i)) % p
        den = (den*(i+1)) % p
    return num*modInverse(den,p)% p

ans = pow(2,n,mod)-1
print((ans-nCr(n,a)-nCr(n,b))%mod)