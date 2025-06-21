import sys
inp = sys.stdin.readline
read = lambda: list(map(int, inp().strip().split()))

def LCS(s, t):
	n, m = len(s), len(t)
	dp = [[0 for i in range(m+1)] for j in range(n+1)]
	for i in range(n+1):
		for j in range(m+1):
			if i == 0 or j == 0:
				dp[i][j] = 0
			elif s[i-1] == t[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	index = dp[n][m]
	ans = [" "]*index
	i, j = n, m
	while index:
		if s[i-1] == t[j-1]:
			ans[index-1] =  s[i-1]
			index -= 1
			i -= 1; j -= 1
		elif dp[i-1][j] > dp[i][j-1]:
			i -= 1
		else:
			j -= 1
	return(("").join(ans))

def solve():
	s1 = inp().strip(); s2 = inp().strip()
	print(LCS(s1, s2))


if __name__ == "__main__":
	solve()