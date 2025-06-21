import numpy as np
s=np.array(list(input()))
t=np.array(list(input()))
is_eq=np.array(s[:,None]==t[None,])
# is_eq[i][j]:sのi文字目とtのj文字目が等しいかどうか
# print(is_eq)
ns=len(s)
nt=len(t)
dp=np.zeros((ns+1,nt+1),np.int64)

# dp[i+1][j+1]:sのi文字目までとtのj文字目までで最長の部分列
# dp[0][j]=0,dp[i][0]=0,dp[n+1][w+1]の値がsとtで最長の部分列の長さ
for i in range(ns): #sのi文字目までの文字列で調査
    dp[i+1][1:]=np.maximum(dp[i][:-1]+is_eq[i],dp[i][1:])#左上からの更新、真上からの更新
    dp[i+1]=np.maximum.accumulate(dp[i+1])#左からの更新
i=ns
j=nt
ans=['']
while i>0 and j>0:
      if dp[i][j]==dp[i-1][j]:
            i-=1
      elif dp[i][j]==dp[i][j-1]:
            j-=1
      else:
            ans.append(s[i-1])
            i-=1
            j-=1
a=''
for _ in range(len(ans)):
      a+=ans.pop()
print(a)

