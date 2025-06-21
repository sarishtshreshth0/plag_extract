import sys
from math import sqrt, gcd, ceil, log
from bisect import bisect
from collections import defaultdict, Counter
inp = sys.stdin.readline
read = lambda: list(map(int, inp().strip().split()))

# sys.setrecursionlimit(10**6)

def fix(arr, d = 0):
	lis = [0]*len(arr)
	if d:
		gcd_ = arr[-1]
		for i in range(len(arr)-1, -1, -1):
			gcd_ = gcd(gcd_, arr[i])
			lis[i] = gcd_
	else:
		gcd_ = arr[0]
		for i in range(len(arr)):
			gcd_ = gcd(gcd_, arr[i])
			lis[i] = (gcd_)
	return(lis)

def solve():
	n = int(inp()); a = read()
	pref_gcd = fix(a)
	suf_gcd = fix(a, 1)
	# print(pref_gcd, suf_gcd)
	ans = pref_gcd[n-1]
	for i in range(n):
		if i == 0:
			ans = max(ans, suf_gcd[i+1])
		elif i == n-1:
			ans = max(ans, pref_gcd[i-1])
		else:
			ans = max(ans, gcd(pref_gcd[i-1], suf_gcd[i+1]))
	print(ans)

	





		

if __name__ == "__main__":
	solve()