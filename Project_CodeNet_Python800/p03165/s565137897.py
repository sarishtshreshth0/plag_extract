s=input()
t=input()
sl=len(s)
tl=len(t)
dp=[[0]*(sl+1) for _ in range(tl+1)]
for i in range(1,tl+1):
  for j in range(1,sl+1):
    if(t[i-1]==s[j-1]):
      dp[i][j]=dp[i-1][j-1]+1
    else:
      dp[i][j]=max(dp[i-1][j],dp[i][j-1])
#print(dp[-1][-1])
i=tl
j=sl
ans=[]
while i>0 and j>0:
  if(t[i-1]==s[j-1]):
    ans.append(t[i-1])
    i=i-1
    j=j-1
  else:
    if(dp[i-1][j]+1>dp[i][j-1]):
      i=i-1
    else:
      j=j-1
#print(ans)
ans.reverse()
print(''.join(ans))