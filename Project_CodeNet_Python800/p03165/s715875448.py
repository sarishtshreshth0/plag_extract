s = input()
t = input()
dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]

for s_i in range(len(s)):
    for t_i in range(len(t)):
        if s[s_i] == t[t_i]:
            dp[s_i+1][t_i+1] = dp[s_i][t_i] + 1
        else:
            dp[s_i+1][t_i+1] = max(dp[s_i][t_i+1], dp[s_i+1][t_i])

ans = []
s_i = len(s)
t_i = len(t)
while s_i > 0 and t_i > 0:
    if dp[s_i][t_i] == dp[s_i][t_i-1]:
        t_i -= 1
    elif dp[s_i][t_i] == dp[s_i-1][t_i]:
        s_i -= 1
    else: #dp[s_i][t_i]  dp[s_i-1][t_i] == 1:
        s_i -= 1
        t_i -= 1
        if t_i >= 0:
            ans.append(t[t_i])


print("".join(ans[::-1]))