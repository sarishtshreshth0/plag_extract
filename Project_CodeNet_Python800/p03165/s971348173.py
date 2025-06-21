s = input()
t = input()
slen, tlen = len(s), len(t)

dp = [[-1 for i in range(tlen + 1)] for j in range(slen + 1)]

for i in range(slen, -1, -1):
    for j in range(tlen, -1, -1):
        if i == slen or j == tlen:
            dp[i][j] = 0
        else:
            if s[i] == t[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])


ans = ""
i, j = 0, 0

while i < slen and j < tlen:
    if dp[i][j] == dp[i + 1][j]:
        i += 1
    elif dp[i][j] == dp[i][j + 1]:
        j += 1
    else:
        ans += s[i]
        i += 1
        j += 1

print(ans)
