import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
s = input()
t = input()

S,T = len(s),len(t)
dp = [[0 for _ in range(T+1)] for _ in range(S+1)]
for i in range(S):
  for j in range(T):
    if s[i]==t[j]:
      dp[i+1][j+1] = max(dp[i][j]+1,dp[i+1][j],dp[i][j+1])
    else:
      dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
# dpの終点から文字列を復元していく
ans=''
while(S>=0 and T>=0):
  if dp[S][T] == dp[S-1][T]:
    S-=1
  elif dp[S][T] == dp[S][T-1]:
    T-=1
  else:
    ans = s[S-1] + ans
    S -=1
    T -=1
print(ans)