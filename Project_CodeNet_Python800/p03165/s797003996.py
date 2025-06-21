s = input()
t = input()
dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
for i in range(len(s) + 1):
    for j in range(len(t) + 1):
        if i < len(s):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j < len(t):
            dp[i][j+1] = max(dp[i][j+1], dp[i][j])
        if i < len(s) and j < len(t) and s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
i, j = len(s), len(t)
now = dp[len(s)][len(t)]
ans = []
while now:
    if dp[i-1][j] == now:
        i -= 1
    elif dp[i][j-1] == now:
        j -= 1
    else:
        i -= 1
        j -= 1
        ans.append(s[i])
        now -= 1
print(''.join(reversed(ans)))