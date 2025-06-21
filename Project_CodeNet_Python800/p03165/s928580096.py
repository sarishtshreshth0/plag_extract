import sys
readline = sys.stdin.readline

S = readline().rstrip()
T = readline().rstrip()

dp = [[0] * (len(T) + 1) for i in range(len(S) + 1)]

for i in range(len(S)):
  for j in range(len(T)):
    if S[i] == T[j]:
      dp[i + 1][j + 1] = dp[i][j] + 1
    else:
      dp[i + 1][j + 1] = max(dp[i][j + 1],dp[i + 1][j])
      
#for d in dp:
#  print(d)
x = len(S)
y = len(T)
ans = ""
while y > 0 and x > 0:
  if dp[x][y] == dp[x][y - 1] + 1 == dp[x - 1][y] + 1:
    ans += T[y - 1]
    y -= 1
    x -= 1
  else:
    if dp[x][y - 1] == dp[x][y]:
      y -= 1
    else:
      x -= 1
  
print(ans[::-1])