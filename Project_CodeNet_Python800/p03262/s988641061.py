import math
n,x = map(int,input().split())
X = list(map(int,input().split()))
diff = []
for i in range(n):
	diff.append(abs(X[i]-x))
res = diff[0]
for i in range(1,n):
	res = math.gcd(res, diff[i])
print(res)


