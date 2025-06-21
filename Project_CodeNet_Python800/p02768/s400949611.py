MOD = 10**9+7
n,a,b=map(int, input().split())
ca = 1
cb = 1
for i in range(n-a+1,n+1):
    ca *= i
    ca%=MOD
for i in range(1,a+1):
    ca *= (pow(i,MOD-2,MOD))
    ca%=MOD
for i in range(n-b+1,n+1):
    cb *= i
    cb%=MOD
for i in range(1,b+1):
    cb*=(pow(i,MOD-2,MOD))
    cb%=MOD
print((pow(2,n,MOD)-1-ca-cb)%MOD)
