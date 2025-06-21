n,a,b = map(int, input().split())

ans = pow(2,n,10**9+7)

nm= 1
dn = 1

for i in range(a):
  nm = (nm * (n-i)) % (10**9+7)
  dn = (dn * (i+1)) % (10**9+7)

ans = (ans - nm*pow(dn,-1,10**9+7) - 1) % (10**9+7)

for i in range(a,b):
  nm = (nm * (n-i)) % (10**9+7)
  dn = (dn * (i+1)) % (10**9+7)

ans = (ans - nm*pow(dn,-1,10**9+7)) % (10**9+7)

print(ans)