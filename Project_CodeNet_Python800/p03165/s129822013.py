s = input()
t = input()
ls = len(s)
lt = len(t)

dp = [[-1 for _ in range(ls+1)] for _ in range(lt+1)]
dp[0] = [0] * (ls+1)

for i in range(lt+1):
  dp[i][0] = 0

for i in range(1,lt+1):
  for j in range(1,ls+1):
    if t[i-1] == s[j-1]:
      dp[i][j] = max((dp[i-1][j-1] + 1),(dp[i-1][j]))
    else:
      dp[i][j] = max((dp[i][j-1]),(dp[i-1][j]))

res = ""
while ls > 0 and lt > 0:
  if dp[lt][ls] == dp[lt][ls-1]:
    ls -= 1
  elif dp[lt][ls] == dp[lt-1][ls]:
    lt -= 1
  else:
    res = s[ls-1] + res
    ls -= 1
    lt -= 1

print(res)