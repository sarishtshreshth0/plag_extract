import math
def count_digits(n):
	res = 0
	while n:
		n = n//10
		res = res+1
	return res
n = int(input())
i =1
ans = 11
while i<=math.sqrt(n):
	if n%i==0:
		a= n//i
		b=i
		u = count_digits(a)
		v =count_digits(b)
		ans = min(ans, max(u,v))
	i=i+1
print(ans)