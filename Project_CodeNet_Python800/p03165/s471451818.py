s=input()
t=input()
ls=len(s)
lt=len(t)
INF=float('inf')

dp=[[0 for i in range(lt+1)] for j in range(ls+1)]
R=[[INF for i in range(lt+1)] for j in range(ls+1)]
for i in range(1,ls+1):
  for j in range(1,lt+1):
    if s[i-1]==t[j-1]:
      dp[i][j]=dp[i-1][j-1]+1
    else:
      dp[i][j]=max(dp[i][j-1],dp[i-1][j])

l=dp[ls][lt]
ans=''
i=ls
j=lt
while l>0:
  if s[i-1]==t[j-1]:
    ans=str(s[i-1])+ans
    l-=1
    i-=1
    j-=1
  elif dp[i][j]==dp[i-1][j]:
    i-=1
  else:
    j-=1
  
print(ans)

