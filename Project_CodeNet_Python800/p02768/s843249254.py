n, a, b = map(int, input().split())
mod = 10**9+7
def nCr(N, R, mod):
	R = min(R, N-R)
	numer = denom = 1
	for i in range(1, R+1):
		numer = numer * (N+1-i) % mod
		denom = denom * i % mod
	return numer * pow(denom, mod-2, mod) % mod


ans = pow(2,n,mod)
ans -= 1
ans -= nCr(n,a,mod)
ans %= mod
ans -= nCr(n,b,mod)
ans %= mod
print (ans)