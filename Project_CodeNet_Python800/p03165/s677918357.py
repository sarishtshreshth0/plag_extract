import numpy as np
s = np.array(list(input().rstrip()))
t = np.array(list(input().rstrip()))
ls, lt = len(s), len(t)
dp = np.zeros((ls+1, lt+1), dtype=np.int64)

for i in range(1, ls+1):
  dp[i, 1:] = dp[i-1, :-1] + (s[i-1] == t)
  dp[i] = np.maximum(dp[i], dp[i-1])
  # print(dp[i])
  dp[i] = np.maximum.accumulate(dp[i])
  # print(dp[i])
answer = ''
x, y = lt, ls
while x > 0 and y > 0:
  # print(answer, x, y)
  if s[y-1] == t[x-1]:
    answer = s[y-1] + answer
    x, y = x-1, y-1
  elif dp[y, x] == dp[y, x-1]:
    x -= 1
  else:
    y -= 1
print(answer)