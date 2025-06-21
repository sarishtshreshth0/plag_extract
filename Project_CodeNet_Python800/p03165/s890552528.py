s = input()
t = input()
s_length = len(s)
t_length = len(t)
dp = [[0] * (s_length + 1) for i in range(t_length + 1)]
for i in range(1, t_length + 1):
    for j in range(1, s_length + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if t[i - 1] == s[j - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
        # print(t[i-1],s[j-1])
        #print(dp)
    #print('---')

answer = ""

while s_length >= 0 and t_length >= 0:
    if dp[t_length][s_length] == dp[t_length - 1][s_length]:
        t_length -= 1
        continue
    elif dp[t_length][s_length] == dp[t_length][s_length-1]:
        s_length -= 1
        continue
    else:
        answer += s[s_length-1]
        s_length -= 1
        t_length -= 1
#print(dp[i][j])
print(answer[::-1])