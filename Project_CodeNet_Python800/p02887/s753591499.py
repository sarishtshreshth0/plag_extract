import sys
# from math import sqrt, gcd, ceil, log
# from bisect import bisect
from collections import defaultdict, Counter
inp = sys.stdin.readline
read = lambda: list(map(int, inp().strip().split()))

# sys.setrecursionlimit(10**6)



def solve():
	n = int(input()); s = inp()
	ans = 1
	for i in range(1, n):
		if s[i-1] != s[i]:
			ans += 1
	print(ans)


		

if __name__ == "__main__":
	solve()