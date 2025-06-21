s=input()
t=input()
l1=len(s)
l2=len(t)
dp=[[0 for _ in range(l1)] for _ in range(l2)]
flg=False
for i in range(l1):
    if flg or t[0]==s[i]:
        flg=True
        dp[0][i]=1
flg=False
for i in range(l2):
    if flg or s[0]==t[i]:
        flg=True
        dp[i][0]=1
for i in range(1,l2):
    for j in range(1,l1):
        if t[i]==s[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
ans=''
i=l2-1
j=l1-1
while i>=0 and j>=0:
    if s[j]==t[i]:
        ans+=s[j]
        i-=1
        j-=1
    else:
        if i==0:
            j-=1
        elif j==0:
            i-=1
        elif dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1
print(ans[::-1])