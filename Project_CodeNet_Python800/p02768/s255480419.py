def cmb(n,r,mod):
	a=1
	b=1
	r = min(r,n-r)
	for i in range(r):
		a = a*(n-i)%mod
		b = b*(i+1)%mod
	return a*pow(b,mod-2,mod)%mod
mod = 10**9+7
n,a,b = list(map(int,input().split()))
ans = pow(2,n,mod)+mod - cmb(n,a,mod) - cmb(n,b,mod)
ans = (ans -1)%mod
print(ans)