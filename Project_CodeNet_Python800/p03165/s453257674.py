import sys
readline = sys.stdin.readline

S = readline().rstrip()
T = readline().rstrip()

# dp[i][j] = Sをi文字目、Tをj文字目まで進めたときの最長
# S[i] == S[j]のとき
# dp[i][j] = dp[i - 1][j - 1] + 1
# S[i] != S[j]のとき
# dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])

# その際、自分がどこから来たか？を記録する
# dp[i - 1][j] > dp[i][j - 1]であれば
# route[i][j] = (i,j)を記録

dp = [[0] * (len(T) + 1) for i in range(len(S) + 1)]
route = [[(0,0)] * (len(T) + 1) for i in range(len(S) + 1)]

for i in range(len(S)):
  for j in range(len(T)):
    if S[i] == T[j]:
      dp[i + 1][j + 1] = dp[i][j] + 1
      route[i + 1][j + 1] = (i,j)
    else:
      if dp[i][j + 1] > dp[i + 1][j]:
        dp[i + 1][j + 1] = dp[i][j + 1]
        route[i + 1][j + 1] = (i,j + 1)
      else:
        dp[i + 1][j + 1] = dp[i + 1][j]
        route[i + 1][j + 1] = (i + 1,j)

# routeのとびさきの文字を追加していく
x,y = len(S),len(T)
ans = ""
while x != 0 and y != 0:
  if S[x - 1] == T[y - 1]:
    ans += S[x - 1]
  x,y = route[x][y]

print(ans[::-1])