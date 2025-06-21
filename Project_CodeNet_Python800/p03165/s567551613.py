from itertools import combinations
s = input()
n = len(s)
t = input()
m = len(t)

dp = [[0 for i in range(m+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = max(dp[i][j],dp[i-1][j-1] + 1)
        elif s[i-1] != t[j-1]:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

i = n
j = m
ans = ""

while i > 0 and j > 0:

    if s[i-1] == t[j-1]:
        ans = s[i-1] + ans 
        i -= 1
        j -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
print(ans)