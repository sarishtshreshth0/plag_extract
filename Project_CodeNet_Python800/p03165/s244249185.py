s = input()
t = input()
ns = len(s)
nt = len(t)

dp = [[0] * (nt + 1) for _ in range(ns + 1)]
for i in range(ns):
    for j in range(nt):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

ans = []
i, j = ns, nt
while dp[i][j]:
    while dp[i - 1][j] == dp[i][j]:
        i -= 1
    while dp[i][j - 1] == dp[i][j]:
        j -= 1
    ans.append(s[i - 1])
    i -= 1
    j -= 1
ans.reverse()
print("".join(ans))
