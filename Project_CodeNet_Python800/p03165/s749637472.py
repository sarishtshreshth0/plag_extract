s=list(input())
t=list(input())
dp=[[0]*(len(s)+1) for i in range(len(t)+1)]
for i in range(1,len(t)+1):
    for j in range(1,len(s)+1):
        if(s[j-1]==t[i-1]):
            dp[i][j]=dp[i-1][j-1] + 1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
# print(dp[len(t)][len(s)])
ans=""
i=len(t)
j=len(s)
while(i!=0 and j!=0):
    if(dp[i][j-1]<dp[i][j]>dp[i-1][j]):
        i-=1
        j-=1
        ans+=t[i]
    elif(dp[i][j]==dp[i-1][j]):
        i-=1
    elif(dp[i][j-1]==dp[i][j]):
        j-=1
print(ans[::-1])     