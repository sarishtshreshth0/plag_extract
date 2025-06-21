s = input()
t = input()

dp = [[0]*(len(s)+1) for i in range(len(t)+1)]

for i in range(1, len(t)+1):
    for j in range(1, len(s)+1):
        if s[j-1] == t[i-1]:
            dp[i][j] = max(dp[i-1][j-1] + 1, dp[i][j-1])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

ans = ''
x = len(t)
y = len(s)
while x>0 and y>0:
    if dp[x][y] == dp[x-1][y]:
        x -= 1
    elif dp[x][y] == dp[x][y-1]:
        y -= 1
    else:
        ans += s[y-1]
        x -= 1
        y -= 1
print(ans[::-1])