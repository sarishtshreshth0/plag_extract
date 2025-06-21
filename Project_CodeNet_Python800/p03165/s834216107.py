a = input()
b = input()
dp = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
            continue
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
m = dp[-1][-1]
ans = ''
i,j=-1,-1
while(len(ans)<m):
    if a[i] == b[j]:
        ans = a[i] + ans
        i-=1
        j-=1
    elif dp[i-1][j] > dp[i][j-1]:
        i-=1
    else:
        j-=1
print(ans)