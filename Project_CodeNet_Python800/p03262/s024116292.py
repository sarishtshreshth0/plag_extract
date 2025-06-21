import math

if __name__ == '__main__':
	n,x = map(int,input().split())
	A = list(map(int,input().split()))
	A.sort(reverse=True)

	B = []
	for i in range(0,n-1):
		tmp = A[i] - A[i+1]
		B.append(tmp)

	ans = abs(x-A[0])
	for j in B:
		ans = math.gcd(ans,j)
	print(ans)

