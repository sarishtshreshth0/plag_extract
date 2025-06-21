def gcd(a, b):
	"""Compute the greatest common divisor of a and b"""
	while b > 0:
		a, b = b, a % b
	return a

def lcm(a, b):
	"""Compute the lowest common multiple of a and b"""
	return a * b // gcd(a, b)

def resolve():
	n = int(input())
	print(lcm(n, 2))
resolve()