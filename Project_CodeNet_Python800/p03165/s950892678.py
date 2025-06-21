s = ["0"] + list(input())
t = ["0"] + list(input())
n, m = len(s), len(t)
dp = [[0] * m for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        if s[i] == t[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
ans = []
c = dp[n - 1][m - 1]
for i in range(n - 1, 0, -1):
    if m == 0:
        break
    for j in range(m - 1, 0, -1):
        if s[i] == t[j] and dp[i][j] == c:
            ans.append(s[i])
            c -= 1
            m = j
            break
        elif dp[i][j] < c:
            break
ans.reverse()
print("".join(ans))