s = input()
t = input()
x = len(s)
y = len(t)
dp = [[0 for _ in range(y+1)] for _ in range(x+1)]

for i in range(x):
	for j in range(y):
		if s[i]==t[j]:
			dp[i+1][j+1] = 1+dp[i][j]
		else:
			dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
i = x
j = y
ans = ''
while i*j!=0:
	if (dp[i][j] == 1 + dp[i-1][j-1]) and (s[i-1]==t[j-1]):
		ans = s[i-1] + ans
		i-=1
		j-=1
			
	else:	
		if dp[i][j] == dp[i-1][j]:
			i-=1
		elif dp[i][j] == dp[i][j-1]:
			j-=1

print(ans)