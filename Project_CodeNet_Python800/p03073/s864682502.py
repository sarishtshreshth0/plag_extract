S = input()
n = len(S)
dp = [[0] * 2 for _ in range(n)]
s = int(S[0])
dp[0][s] = 0
dp[0][1-s] = 1
for i, s in enumerate(S[1:], 1):
    s = int(s)
    dp[i][s] = dp[i-1][1-s]
    dp[i][1-s] = dp[i-1][s] + 1
print(min(dp[n-1]))
