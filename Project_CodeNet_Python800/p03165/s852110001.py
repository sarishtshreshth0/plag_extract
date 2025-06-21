s = input()
s_len = len(s)
t = input()
t_len = len(t)
dp = [[0] * (t_len + 1) for _ in range(s_len + 1)]
for i in range(s_len):
    S = s[i]
    for j in range(t_len):
        T = t[j]
        ni = i + 1
        nj = j + 1
        if S == T:
            dp[ni][nj] = max(dp[ni][nj], dp[i][j] + 1, dp[i][nj], dp[ni][j])
        else:
            dp[ni][nj] = max(dp[ni][nj], dp[i][nj], dp[ni][j])

nagasa = dp[s_len][t_len]

a = s_len
b = t_len
ans = []
while nagasa > 0:
    if dp[a][b] == nagasa:
        a -= 1
    elif dp[a + 1][b] == nagasa:
        b -= 1
    else:
        ans.append(s[a])
        nagasa -= 1
ans = ans[::-1]
print(*ans, sep="")
