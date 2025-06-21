def gcd(a,b): return a if b==0 else gcd(b,a%b)

n = int(input())
a = [int(x) for x in input().split()]
pref = [x for x in a]
suff = [x for x in a]
for i in range(1,n):
	pref[i] = gcd(pref[i-1],a[i])
for i in range(n-2,-1,-1):
	suff[i] = gcd(suff[i+1],a[i])

print(max([pref[-2],suff[1]]+[gcd(pref[i-1],suff[i+1]) for i in range(1,n-1)])) 