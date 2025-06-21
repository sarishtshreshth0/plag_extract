s=input()
t=input()

m=len(s)
n=len(t)

dp=[[0]*(n+1) for _ in range(m+1)]
trans=[[(-1,-1)]*(n+1) for _ in range(m+1)]

for i in range(m):
    for j in range(n):
        if s[i]==t[j]:
            dp[i+1][j+1]=dp[i][j]+1
            trans[i+1][j+1]=(i,j)
        else:
            if dp[i][j+1]>dp[i+1][j]:
                dp[i+1][j+1]=dp[i][j+1]
                trans[i+1][j+1]=(i,j+1)
            else:
                dp[i+1][j+1]=dp[i+1][j]
                trans[i+1][j+1]=(i+1,j)

ans=''

i=m
j=n
while i>0 and j>0:
    if s[i-1]==t[j-1]:
        ans=str(s[i-1])+ans
    i,j=trans[i][j]

print(ans)