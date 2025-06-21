
S=input()
T=input()

s=len(S)
t=len(T)
dp=[[0 for i in range(s+1)] for j in range(t+1)]


for i in range(1,t+1):
  for j in range(1,s+1):
    if S[j-1]==T[i-1]:
      dp[i][j]=dp[i-1][j-1]+1
    else:
      dp[i][j]=max(dp[i-1][j],dp[i][j-1])
  
arr=[]
while(i>0 and j>0):
  if S[j-1]==T[i-1]:
    arr+=[j-1]
    j-=1
    i-=1
  else:
    if dp[i-1][j]>dp[i][j-1]:
      i-=1
    else:
      j-=1
arr.sort()
for i in arr:
  print(S[i],end="")
