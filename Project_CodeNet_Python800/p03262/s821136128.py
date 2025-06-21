import fractions
n,x = map(int,input().split())
a = list(map(int,input().split()))
res,ans = [],0
for i in range(n):
	res.append(abs(a[i]-x))
if len(res) > 3:
	D = fractions.gcd(res[0],res[1])
	for j in range(2,len(res)-2):
		D = fractions.gcd(D,res[j])
	ans = D
else:
	ans = min(res)
print(ans)