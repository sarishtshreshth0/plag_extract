from sys import stdin, stdout, setrecursionlimit
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
import math

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())
rlf = lambda: map(float, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')

def main():
	s, t = rll()[0], rll()[0]
	m, n = len(s), len(t)
	dp = [[0 for __ in range(n)] for _ in range(m)]
	dp[0][0] = 1 if s[0] == t[0] else 0
	for r in range(1, m):
		dp[r][0] = max(dp[r-1][0], 1 if s[r] == t[0] else 0)
	for c in range(1, n):
		dp[0][c] = max(dp[0][c-1], 1 if s[0] == t[c] else 0)
	for r in range(1, m):
		for c in range(1, n):
			dp[r][c] = max(dp[r-1][c], dp[r][c-1])
			if s[r] == t[c]:
				dp[r][c] = max(dp[r][c], 1 + dp[r-1][c-1])
	ans = deque()
	r, c = m-1, n-1
	while r >= 0 and c >= 0:
		if s[r] == t[c]:
			ans.appendleft(s[r])
			r -= 1
			c -= 1
		else:
			U = dp[r-1][c] if r > 0 else NINF
			L = dp[r][c-1] if c > 0 else NINF
			if L >= U:
				c -= 1
			else:
				r -= 1
	print("".join(x for x in ans))
	stdout.close()

if __name__ == "__main__":
	main()