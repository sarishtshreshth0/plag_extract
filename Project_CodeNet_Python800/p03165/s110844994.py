S = input()
T = input()

dp = [[0] * (len(T) + 1) for i in range(len(S) + 1)]

for i in range(len(S)):
  for j in range(len(T)):
    if S[i] == T[j]:
      dp[i + 1][j + 1] = dp[i][j] + 1
    else:
      dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
      
s = len(S)
t = len(T)
ans = ""
while s > 0 and t > 0:
  if dp[s][t] == dp[s - 1][t]:
    s -= 1
  elif dp[s][t] == dp[s][t - 1]:
    t -= 1
  else:
    ans += S[s - 1]
    s -= 1
    t -= 1
    
print(ans[::-1])