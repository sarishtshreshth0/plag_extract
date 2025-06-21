s=input()
t=input()
dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]
for i in range(len(s)):
  for j in range(len(t)):
    if s[i]==t[j]:
      dp[i+1][j+1]=dp[i][j]+1
    else:
      dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
len_=dp[len(s)][len(t)]
s_now=len(s)
t_now=len(t)
ans=''
if len_==0:
  print(ans)
  exit()
while len_>0:
  if s[s_now-1]==t[t_now-1]:
    ans=ans+s[s_now-1]
    len_+=-1
    s_now+=-1
    t_now+=-1
    
  else:
    if dp[s_now][t_now]==dp[s_now][t_now-1]:
      t_now=t_now-1
    elif dp[s_now][t_now]==dp[s_now-1][t_now]:
      s_now=s_now-1
ans=ans[::-1]
print(ans)

