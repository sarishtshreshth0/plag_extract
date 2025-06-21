s = input()
t = input()
s_length = len(s)
t_length = len(t)

dp = [[0]*(t_length + 1) for _ in range(s_length + 1)]
for i in range(s_length):
    for j in range(t_length):
        if s[i]==t[j]:
            dp[i+1][j+1] = max(dp[i][j]+1,dp[i+1][j+1])
        
        dp[i+1][j+1] = max(dp[i+1][j+1],dp[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j+1])

ans=""
i = s_length
j = t_length
while i > 0 and j > 0:
    if dp[i][j] == dp[i-1][j]:
        i-=1
    elif dp[i][j] == dp[i][j-1]:
        j-=1
    else:
        ans = s[i-1] + ans
        i-=1
        j-=1
print(ans)
