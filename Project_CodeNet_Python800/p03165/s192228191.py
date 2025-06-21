def LCS_iter(s1, s2):
	dp = [[-10000 for i in range(len(s2) + 1)] for i in range(len(s1) + 1)]
	ans = [['' for i in range(len(s2) + 1)] for i in range(len(s1) + 1)]
	for i in range(len(s2) + 1):
		dp[0][i] = 0
	for i in range(len(s1) + 1):
		dp[i][0] = 0
	i = 1
	j = 1
	while i <= len(s1):
		while j <= len(s2):
			if s1[i - 1] == s2[j - 1]:
				dp[i][j] = 1 + dp[i - 1][j - 1]
				ans[i][j] = 'cross'
			else:
				if dp[i - 1][j] > dp[i][j - 1]:
					dp[i][j] = dp[i - 1][j]
					ans[i][j] = 'up'
				else:
					dp[i][j] = dp[i][j - 1]
					ans[i][j] = 'left'
			j += 1
		i += 1
		j = 1
	i = len(s1)
	j = len(s2)
	s = ''
	while i >= 0 and j >= 0:
		if ans[i][j] == 'cross':
			s += s1[i - 1]
			i -= 1
			j -= 1
		elif ans[i][j] == 'up':
			i -= 1
		else:
			j -= 1
	return s[::-1]
 
 
s1 = input()
s2 = input()
 
print(LCS_iter(s1, s2))