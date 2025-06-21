s = input()
t = input()
dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

for i in range(1, len(s)+1):
  for j in range(1, len(t)+1):
    dp[i][j] = max(dp[i][j], dp[i][j-1], dp[i-1][j])
    if s[i-1] == t[j-1]:
      dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

ans = ""
i, j = len(s), len(t)
while i > 0 and j > 0:
  if dp[i][j] == dp[i][j-1]:
    j -= 1
  elif dp[i][j] == dp[i-1][j]:
    i -= 1
  else:
    ans = s[i-1] + ans
    i -= 1
    j -= 1
print(ans)