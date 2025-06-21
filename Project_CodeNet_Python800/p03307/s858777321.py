import math

if __name__ == '__main__':

	m = 2
	n = int(input())

	ans = n * m // math.gcd(m,n)
	print(ans)
