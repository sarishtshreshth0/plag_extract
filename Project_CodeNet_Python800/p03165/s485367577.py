s = input()
t = input()
n_s = len(s)
n_t = len(t)

dp = [[0]*(n_t+1) for _ in range(n_s+1)]
#dp[i][j]はsのi文字目までとtのj文字目までのLCSの長さ

for i in range(n_s+1):
    for j in range(n_t+1):
        if i == 0 or j == 0:
            continue
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if s[i-1] == t[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

sna = ""
while n_s > 0 and n_t > 0:
    if dp[n_s][n_t] == dp[n_s-1][n_t]:
        n_s -= 1
    elif dp[n_s][n_t] == dp[n_s][n_t-1]:
        n_t -= 1
    else:
        sna += s[n_s-1]
        n_s -= 1
        n_t -= 1
ans = ""
for i in range(len(sna))[::-1]:
    ans += sna[i]
print(ans)