s = input()
t = input()

ls = len(s)
lt = len(t)

dp = [[0 for _ in range(lt + 1)] for __ in range(ls + 1)]

for ns in range(ls):
    for nt in range(lt):
        if s[ns] == t[nt]:
            dp[ns + 1][nt + 1] = max(dp[ns][nt] + 1, dp[ns + 1][nt + 1])
        dp[ns + 1][nt + 1] = max(dp[ns + 1][nt + 1], dp[ns + 1][nt], dp[ns][nt + 1])

ans = ''
i, j = ls, lt
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        ans = s[i - 1] + ans
        i -= 1
        j -= 1
print(ans)
