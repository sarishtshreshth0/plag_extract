s1=input()
s2=input()
n1=len(s1)
n2=len(s2)
dp=[[0 for i in range(n2+1)] for j in range(n1+1)] 
for i in range(1,n1+1):
    for j in range(1,n2+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1]) 
s=""
i,j=n1,n2
while dp[i][j]:
    if dp[i][j]==dp[i][j-1]:
        j-=1 
    elif dp[i][j]==dp[i-1][j]:
        i-=1 
    else:
        s=s1[i-1]+s
        i-=1 
        j-=1 
print(s)