def gcd(a,b):
	if a%b==0:return b
	else:return gcd(b,a%b)
INF=10**9
ans=INF
n,X=map(int,input().split())
x=list(map(int,input().split()))
if n==1:
	print(abs(X-x[0]))
else:
	for i in range(n-1):
		tmp=gcd(abs(X-x[i]),abs(X-x[i+1]))
		ans=min(ans,tmp)
	print(ans)
