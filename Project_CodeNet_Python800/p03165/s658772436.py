s=input()
t=input()

S=len(s)+1
T=len(t)+1

dp=[[0]*T for i in range(S)]

for i in range(1,S):
  for j in range(1,T):
    if s[i-1]==t[j-1]:
      dp[i][j] = max(dp[i][j],dp[i-1][j-1] + 1)
    dp[i][j] = max(dp[i][j],dp[i-1][j]) 
    dp[i][j] = max(dp[i][j],dp[i][j-1])
    
res=""
i=len(s)
j=len(t)
while i>0 and j>0:
  #(i-1,j)->(i,j)に更新した場合
  if dp[i][j] == dp[i-1][j]:
    i -= 1
  #(i,j-1)->(i,j)に更新した場合
  elif dp[i][j] == dp[i][j-1]:
    j -= 1
  #s[i]=t[j]であり、(i-1,j-1)->(i,j)に更新した場合
  else:
    res = s[i-1] + res
    i -= 1
    j -= 1
print(res)