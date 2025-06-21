S = input()
T = input()
s,t = len(S),len(T)
dp = [[0]*(t+1) for _ in range(s+1)]

for i in range(1,s+1):
  for j in range(1,t+1):
    if S[i-1]==T[j-1]:
      dp[i][j] = dp[i-1][j-1]+1
    else:
      dp[i][j] = max(dp[i-1][j],dp[i][j-1])

ans = ''
n,m = s,t
while n>0 and m>0:
  if dp[n][m]==dp[n-1][m]:
    n -= 1
  elif dp[n][m]==dp[n][m-1]:
    m -= 1
  else:
    ans = S[n-1] + ans
    n -= 1
    m -= 1
print(ans)