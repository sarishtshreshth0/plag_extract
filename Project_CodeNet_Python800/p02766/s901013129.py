import sys
input = sys.stdin.readline

def pn(x, n):
	if x // n: return pn(x // n, n) + str(x % n)
	return str(x % n)
n, k = map(int, input().split())
print(len(pn(n, k)))