from sys import stdin, stdout
from collections import deque, defaultdict
import math as m

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')

def main():
	s = rll()[0]
	t = rll()[0]
	m, n = len(s), len(t)
	dp = [[0 for __ in range(n)] for _ in range(m)]

	#dp[i][j] = LCs of s0,...,si and t0,...,tj

	def pprint(M):
		for row in M:
			print(row)
		print("~~~")
	
	dp[0][0] = 1 if s[0] == t[0] else 0
	for c in range(1, n):
		dp[0][c] = max(dp[0][c-1], 1 if s[0] == t[c] else 0)
	for r in range(1, m):
		dp[r][0] = max(dp[r-1][0], 1 if s[r] == t[0] else 0)

	for r in range(1, m):
		for c in range(1, n):
			dp[r][c] = max(dp[r][c], dp[r-1][c], dp[r][c-1])
			if s[r] == t[c]:
				dp[r][c] = max(dp[r][c], 1 + dp[r-1][c-1])

	ans = deque()
	i, j = m - 1, n - 1
	while i >= 0 and j >= 0:
		if s[i] == t[j]:
			ans.appendleft(s[i])
			i -= 1
			j -= 1
		else:
			up, left = NINF, NINF
			if i - 1 >= 0:
				up = dp[i-1][j]
			if j - 1 >= 0:
				left = dp[i][j-1]
			if up >= left:
				i -= 1
			else:
				j -= 1
	print("".join(x for x in ans))
	stdout.close()

if __name__ == "__main__":
	main()