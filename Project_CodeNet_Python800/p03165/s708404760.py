s = list(input())
t = list(input())
ns=len(s)
nt=len(t)
dp=[[0]*(nt+1) for _ in range(ns+1)]
for i in range(ns):
    for j in range(nt):
        if s[i]==t[j]:
            dp[i+1][j+1]=max(dp[i+1][j+1], dp[i][j]+1)
        else:
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
ans=[]
i,j=ns,nt
while i!=0 and j!=0:
    if dp[i][j]==dp[i-1][j]:
        i-=1
    elif dp[i][j]==dp[i][j-1]:
        j-=1
    elif dp[i][j]==dp[i-1][j-1]+1:
        ans=[s[i-1]]+ans
        i-=1
        j-=1
print(''.join(ans))