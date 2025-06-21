S = input()
T = input()
m = len(S)
n = len(T)
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j-1], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# print(dp)
i, j = m, n
ans = ''
while dp[i][j] > 0:
    if S[i-1] == T[j-1]:
        ans += S[i-1]
        i -= 1
        j -= 1
    elif dp[i-1][j] == dp[i][j]:
        i -= 1
    else:
        j -= 1
ans = ans[::-1]
print(ans)
