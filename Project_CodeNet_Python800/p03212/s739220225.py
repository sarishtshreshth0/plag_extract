from itertools import product
n=int(input())
ans=0
for k in range(3,10):
  dp=list(product("753",repeat=k))
  for i in range(len(dp)):
    if n>=int("".join(dp[i])) and "3" in dp[i] and "5" in dp[i] and "7" in dp[i]:
      ans+=1
print(ans)