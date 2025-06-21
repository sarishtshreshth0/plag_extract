

s = input()
l_s = len(s)
t = input()
l_t = len(t)

dp = list([0 for _ in range(l_t+1)] for _ in range(l_s+1))

for i in range(l_s):
    for j in range(l_t):
        #dp[i+1][j+1]  = ...
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i][j]+1 , dp[i+1][j] , dp[i][j+1])
        else:
            dp[i+1][j+1] = max(dp[i][j], dp[i+1][j] , dp[i][j+1])

ans = []
l = dp[-1][-1]
i = l_s
j = l_t
while l != 0:
    if s[i-1] == t[j-1]:
        ans.append(s[i-1])
        i -= 1
        j -= 1
        l -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        j -= 1

print("".join(ans[::-1]))


