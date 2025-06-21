s=input()
t=input()
dp=[[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
#print(lcs(s,t,0,0," ",dp))

for i in range(1,len(s)+1):
    for j in range(1,len(t)+1):
        if s[i-1]==t[j-1]:
            dp[i][j]=1+(dp[i-1][j-1])
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

x=len(s)
y=len(t)
ans=""
while x!=0 and y!=0:
    if dp[x-1][y]==dp[x][y]:
        x-=1
    elif dp[x][y-1]==dp[x][y]:
        y-=1
    else:
        ans=t[y-1]+ans
        x-=1
        y-=1
print(ans)