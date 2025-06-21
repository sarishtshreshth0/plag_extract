s = input()
t = input()
n,m = len(s),len(t)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if i != n and j != m and s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j] + 1)
        if i != n:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j != m:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j])
ans = ""
i = n
j = m
while i > 0 or j > 0:
    if i > 0 and dp[i][j] == dp[i-1][j]:
        i -= 1
    elif j > 0 and dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        i -= 1
        j -= 1
        ans = s[i] + ans
print(ans)
