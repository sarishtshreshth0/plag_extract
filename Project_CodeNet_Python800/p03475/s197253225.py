N=int(input())
dp=[0]*N
for i in range(N-1):
  C,S,F=map(int,input().split())
  for j in range(i+1):
    if dp[j]>S:
      if (dp[j]-S)%F!=0:
        dp[j]=((dp[j]-S)//F+1)*F+S
    else:
      dp[j]=S
    dp[j]+=C
for i in range(N):
  print(dp[i])