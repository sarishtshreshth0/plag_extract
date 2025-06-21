s=input()
t=input()
n=len(s)
m=len(t)
dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
  for j in range(m):
    if s[i]==t[j]:dp[i+1][j+1]=dp[i][j]+1
    else:dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j],dp[i+1][j+1])
ans=''
while n*m:
  if s[n-1]==t[m-1]:
    ans+=s[n-1]
    n-=1
    m-=1
  else:
    if dp[n-1][m]>dp[n][m-1]:n-=1
    else:m-=1
print(ans[::-1])