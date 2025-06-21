s=str(input())
t=str(input())
len_s=len(s)
len_t=len(t)
ans=""
dp=[[0 for i in range(len_t+1)] for j in range(len_s+1)]
for i in range(len_s):
    for j in range(len_t):
        if s[i]==t[j]:
            dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+1)
        dp[i+1][j+1]=max(dp[i+1][j+1],dp[i+1][j])
        dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j+1])

while len_s>0 and len_t>0:
    if dp[len_s][len_t]==dp[len_s-1][len_t]:
        len_s-=1
    elif dp[len_s][len_t]==dp[len_s][len_t-1]:
        len_t-=1
    else:
        ans=s[len_s-1]+ans
        len_s-=1
        len_t-=1
print(ans)
