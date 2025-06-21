def solve():
  ans = ''
  S = input()
  T = input()
  n,m = len(S),len(T)
  dp = [[0]*(m+1) for _ in range(n+1)]
  for i in range(1,n+1):
    for j in range(1,m+1):
      if S[i-1]==T[j-1]:
        dp[i][j] = dp[i-1][j-1]+1
      else:
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
  i,j = n,m
  while i>0 and j>0:
    if dp[i-1][j]==dp[i][j]:
      i -= 1
    elif dp[i][j-1]==dp[i][j]:
      j -= 1
    else:
      ans = S[i-1]+ans
      i -= 1
      j -= 1
  return ans
print(solve())