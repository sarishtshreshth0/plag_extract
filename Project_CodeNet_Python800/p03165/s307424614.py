s = input()
t = input()

ssize = len(s)
tsize = len(t)

# dp[i][j]: sのi文字目まで、tのj文字目までのLongestCommonSubsequence
dp = [[0] * (tsize+1) for _ in range(ssize+1)]

for i in range(1, ssize+1):
    for j in range(1, tsize+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i, j = ssize, tsize

ans = ""
while i > 0 and j > 0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        ans = s[i-1] + ans
        i -= 1
        j -= 1

print(ans)