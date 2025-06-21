n,a,b=map(int,input().split())
MOD=10**9+7
afac=1
for i in range(1,a+1):
  afac=(i*afac)%MOD
afac=pow(afac,MOD-2,MOD)
bfac=1
for i in range(1,b+1):
  bfac=(i*bfac)%MOD
bfac=pow(bfac,MOD-2,MOD)
thing1=1
for i in range(n,n-a,-1):
  thing1=(i*thing1)%MOD
thing2=1
for i in range(n,n-b,-1):
  thing2=(i*thing2)%MOD
print((pow(2,n,MOD)-1-thing1*afac-thing2*bfac)%MOD)