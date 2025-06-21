s = input()
t = input()
ls = len(s)
lt = len(t)
dp = [[0 for j in range(lt+1)] for i in range(ls+1)]
for i in range(1, ls+1):
  for j in range(1, lt+1):
    if s[i-1] == t[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
ans = ""
length = dp[ls][lt]
i = ls
j = lt
while length > 0:
  if s[ls-1] == t[lt-1]:
    ans = s[ls-1] + ans
    ls -= 1
    lt -= 1
    length -= 1
  elif dp[ls-1][lt] == length:
    ls -= 1
  else:
    lt -= 1
print(ans)