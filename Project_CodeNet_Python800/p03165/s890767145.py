s=input()
t=input()
S,T=len(s),len(t)
dp=[[0]*(T+1) for _ in range(S+1)]
for i in range(S):
    for j in range(T):
        if s[i]==t[j]:
            dp[i+1][j+1]=dp[i][j]+1
        else:
            dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])

l=dp[S][T]
x,y=S,T
ans=[0]*l
while l>0:
    if s[x-1]==t[y-1]:
        ans[l-1]=s[x-1]
        l-=1
        x-=1
        y-=1
    else:
        if dp[x][y]==dp[x-1][y]:x-=1
        else:y-=1
print("".join(ans))