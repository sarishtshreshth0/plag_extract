s = input()
t = input()
mx = 0
mxp = [-1, -1]
dp = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
for i in range(len(s)):
	for j in range(len(t)):
		if s[i] == t[j]:
			dp[i + 1][j + 1] = 1 + dp[i][j]
		else:
			dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
		if dp[i + 1][j + 1] > mx:
			mx = dp[i + 1][j + 1]
			mxp = [i + 1, j + 1]
if mx == 0:
	print()
else:
	ans = ''
	x = mxp[0]
	y = mxp[1]
	while dp[x][y]:
		if s[x - 1] == t[y - 1]:
			ans += s[x - 1]
			x -= 1
			y -= 1
		else:
			if dp[x - 1][y] > dp[x][y - 1]:
				x -= 1
			else:
				y -= 1
	print(ans[::-1])
