s=input()
t=input()
n=len(s)
m=len(t)
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1]==t[j-1]:
            if i>0 and j>0:
                dp[i][j]=dp[i-1][j-1]+1
        else:
            if i>0:
                dp[i][j]=max(dp[i][j],dp[i-1][j])
            if j>0:
                dp[i][j]=max(dp[i][j],dp[i][j-1])
leng=dp[n][m]
i,j=n,m
ans=""
while leng>0:
    if s[i-1]==t[j-1]:
        ans+=s[i-1]
        i-=1
        j-=1
        leng-=1
    else:
        if dp[i-1][j]==dp[i][j]:
            i-=1
        elif dp[i][j-1]==dp[i][j]:
            j-=1
print(ans[::-1])