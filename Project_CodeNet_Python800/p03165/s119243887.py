s=input()
t=input()

dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]
ans=[[(-1,-1) for _ in range(len(t)+1)] for _ in range(len(s)+1)]

for i,c in enumerate(s):
    for j,d in enumerate(t):
        if c==d:
            dp[i+1][j+1]=dp[i][j]+1
            ans[i+1][j+1]=(i,j)
        else:
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
            ans[i+1][j+1]=ans[i][j+1] if dp[i+1][j+1]==dp[i][j+1] else ans[i+1][j]

i=len(s)
j=len(t)
ss=['']*dp[i][j]
l=dp[i][j]-1
while i>0 and j>0:
    i,j=ans[i][j]
    if i>-1:
        ss[l]=s[i]
        l-=1

print(''.join(ss))
