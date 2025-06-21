N,A,B = map(int,input().split())

mod = 10**9 + 7
def cmb(n,r,mod):
	a=1
	b=1
	r = min(r,n-r)
	for i in range(r):
		a = a*(n-i)%mod
		b = b*(i+1)%mod
	return a*pow(b,mod-2,mod)%mod

all = pow(2,N,mod) + mod
nCa = cmb(N,A,mod)
nCb = cmb(N,B,mod)

ans = all - nCa - nCb
print((ans-1)%mod)