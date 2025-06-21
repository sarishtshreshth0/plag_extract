n,a,b = map(int,input().split())

mod = 10**9+7

ans = 1
r = 2
m = n
while(True):
    if(m%2 == 1):
        ans *= r
        ans %= mod
    r = r**2
    r %= mod
    m = m//2
    if(m == 0):
        break

a = max(a,n-a)
b = max(b,n-b)
base = []
rbase = [0,1]
c = min(a,b)
d = max(a,b)

bas = 1
for i in range(n,c,-1):
    bas *= i
    bas %= mod
    base.append(bas)

#0からn-cまでの逆元
rbase = [0,1]
for i in range(2,n-c+1):
    q = mod//i
    r = mod % i
    rbase.append(-q * rbase[r] % mod)
rbases = []
rbas = 1
for i in range(1,n-c+1):
    rbas *= rbase[i]
    rbas %= mod
    rbases.append(rbas)

a_ = base[n-c-1]*rbases[n-c-1]%mod
if(d == n):
    b_ = 1
else:
    b_ = base[n-d-1]*rbases[n-d-1]%mod
print((ans - a_ - b_ - 1)%mod)
