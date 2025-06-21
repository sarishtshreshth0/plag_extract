s = list(input())
t = list(input())
lens = len(s)
lent = len(t)
dp = [[0]*(lens+1) for _ in range(lent+1)]

for i in range(1,lent+1):
    x = t[i-1]
    for j in range(1,lens+1):
        y = s[j-1]
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        if x == y:
            dp[i][j] = max(dp[i][j],dp[i-1][j-1]+1)

m = lent
n = lens
ans = ""
while m>0 and n>0:
    if dp[m][n] == dp[m-1][n]:
        m -= 1
        continue
    if dp[m][n] == dp[m][n-1]:
        n -= 1
        continue
    m -= 1
    n -= 1
    ans = t[m]+ans

print(ans)