s = input()
t = input()
x = len(s)
y = len(t)
dp = [[0]*(y+1) for _ in range(x+1)]
for i in range(x):
    for j in range(y):
        if s[i] == t[j]: dp[i+1][j+1] = dp[i][j] + 1
        else: dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
        
# for i in range(x+1): print(dp[i])
ans = ""
i = x
j = y
while i > 0 and j > 0:
    if dp[i][j] == dp[i-1][j]: i -= 1
    elif dp[i][j] == dp[i][j-1]: j -= 1
    else:
        ans = s[i-1]+ans
        i -= 1
        j -= 1
print(ans)