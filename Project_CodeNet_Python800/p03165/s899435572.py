s,t=input(),input()
S,T=len(s),len(t)
dp=[[0]*(T+1) for _ in range(S+1)]
for i in range(1,S+1):
    for j in range(1,T+1):
        if s[i-1]==t[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

i,j=S,T
ans=''
while min(i,j)>0:
        if dp[i][j]==dp[i][j-1]:
            j-=1
        elif dp[i][j]==dp[i-1][j]:
            i-=1
        else:
            ans+=s[i-1]
            i-=1 ; j-=1
print(ans[::-1])