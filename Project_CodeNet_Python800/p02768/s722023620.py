n,a,b=map(int,input().split())

def cmb(n, r, p):
	if (r < 0) or (n < r):
		return 0
	s = 1
	for i in range(r):
		s = (s * (n-i)) % p
	return (s * factinv[r]) % p

p = 10 ** 9 + 7
N = 2 * 10 ** 5  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
	fact.append((fact[-1] * i) % p)
	inv.append((-inv[p % i] * (p // i)) % p)
	factinv.append((factinv[-1] * inv[-1]) % p)

ans = pow(2, n, p)
ans -= cmb(n, a, p)
ans -= cmb(n, b, p)
ans -= 1
print(ans % p)