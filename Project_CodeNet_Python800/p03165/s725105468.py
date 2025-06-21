s = input()
t = input()

inf = pow(10, 4)
dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
key = [[0]*(len(t)+1) for _ in range(len(s)+1)]
for i in range(len(s)+1):
  for j in range(len(t)+1):
    if i == 0 and j == 0:
      continue
    if i == 0:
      dp[i][j] = dp[i][j-1]
      continue
    if j == 0:
      dp[i][j] = dp[i-1][j]
      continue
    if s[i-1] == t[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
      key[i][j] = (i-1)*inf+(j-1)
    else:
      if dp[i-1][j] > dp[i][j-1]:
        dp[i][j] = dp[i-1][j]
        key[i][j] = key[i-1][j]
      else:
        dp[i][j] = dp[i][j-1]
        key[i][j] = key[i][j-1]

ans = []
i, j = key[len(s)][len(t)]//inf, key[len(s)][len(t)]%inf
while True:
  if s[i] == t[j]:
    ans.append(s[i])
  if i == 0 or j == 0:
    break
  i, j = key[i][j]//inf, key[i][j]%inf

ans.reverse()
print("".join(ans))