s = input()
t = input()
len_s = len(s)
len_t = len(t)
dp = [[0]*(len_t+1) for _ in range(len_s+1)]
# dp[i][j]はi、j文字目までのs[i],t[j]で、最長の部分列の長さ
for i in range(len_s):
    for j in range(len_t):
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i][j]+1, dp[i+1][j], dp[i][j+1])

        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
#print(dp)
ans = ""
while len_t > 0 and len_s > 0:
    if dp[len_s][len_t] == dp[len_s-1][len_t]:
        len_s -= 1
    elif dp[len_s][len_t] == dp[len_s][len_t-1]:
        len_t -= 1
    else:
        ans += s[len_s-1]
        len_s -= 1
        len_t -= 1
print(ans[::-1])