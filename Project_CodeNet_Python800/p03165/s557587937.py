s=input()
t=input()
N,M=len(s),len(t)
dp=[[0]*(M+1) for i in range(N+1)]
dp2=[[0]*(M+1) for i in range(N+1)]
for i in range(N):
    for j in range(M):
        if s[i]==t[j]:
            dp[i+1][j+1]=dp[i][j]+1
            dp2[i+1][j+1]=3
        elif dp[i][j+1]<dp[i+1][j]:
            dp[i+1][j+1]=dp[i+1][j]
            dp2[i+1][j+1]=1
        else:
            dp[i+1][j+1]=dp[i][j+1]
            dp2[i+1][j+1]=2
a=[]
while i>=0 and j>=0:
    if dp2[i+1][j+1]==1:
        j-=1
    elif dp2[i+1][j+1]==2:
        i-=1
    else:
        a.append(s[i])
        i-=1
        j-=1
print(*reversed(a),sep='')