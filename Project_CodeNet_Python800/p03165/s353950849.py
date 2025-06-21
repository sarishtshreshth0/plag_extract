s=input()
t=input()

l1,l2 = len(s),len(t)

dp = [[0]*(l2+1) for _ in range(l1+1)]
memo = [['']*(l2+1) for _ in range(l1+1)]

for i in range(1,l1+1):
  for j in range(1,l2+1):
    if s[i-1]==t[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
      memo[i][j] = s[i-1]
    else:
      if dp[i-1][j] >= dp[i][j-1]:
        dp[i][j] = dp[i-1][j]
        memo[i][j] = (i-1,j)
      else:
        dp[i][j] = dp[i][j-1]
        memo[i][j] = (i,j-1)
      
i,j = l1,l2
ans = []
while i > 0 and j > 0:
  if len(memo[i][j]) == 2:
    i, j = memo[i][j]
  else:
    ans.append(memo[i][j])
    i, j = i-1, j-1
    
print(''.join(ans[::-1]))