s=list(input())
t=list(input())
dp=[[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(t)):
        if s[i]==t[j]:
            dp[i+1][j+1]=max(dp[i][j]+1,dp[i+1][j],dp[i][j+1])
        else:
            dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])

path=[]

lens=len(s)
lent=len(t)
while lens>-1 and lent>-1 :
    if dp[lens][lent]==dp[lens-1][lent]:
        lens-=1
    elif dp[lens][lent]==dp[lens][lent-1]:
        lent-=1
    else:
        path.append(lens)
        lens-=1
        lent-=1

path.sort()
if path==[]:
    print("")
else:
    for i in path:
    	print(s[i-1],end="")