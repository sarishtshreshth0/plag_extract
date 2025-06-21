s=input()
t=input()
n=len(s)
m=len(t)
dp=[[0 for x in range(n+1)] for y in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if(s[j-1]==t[i-1]):
            dp[i][j]=1+dp[i-1][j-1]
        else:
            temp=max(dp[i-1][j],dp[i][j-1])
            dp[i][j]=temp
i,j=m,n
ans=''
while (i>0 and j>0):
    if(s[j-1]==t[i-1]):
        ans+=s[j-1]
        i-=1
        j-=1
    else:
        if(dp[i-1][j]>dp[i][j-1]):
            i-=1
        else:
            j-=1
print(ans[::-1])