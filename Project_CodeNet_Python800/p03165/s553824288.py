s = input()
t = input()
n = len(s)
m = len(t)
dp = [[0 for j in range(1 + m)] for i in range(1 + n)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
res = ""
i, j = n, m
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        res = s[i - 1] + res
        i -= 1
        j -= 1
print(res)