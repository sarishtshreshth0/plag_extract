s1=input()
s2=input()
n1,n2=len(s1),len(s2)
dp=[[-1 for j in range(n2+1)] for i in range(n1+1)]
for i in range(n1,-1,-1):
    for j in range(n2,-1,-1):
        if i==n1 or j==n2:
            dp[i][j]=0
        else:
            if s1[i]==s2[j]:
                dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])
n=""
i,j=0,0
while i<n1 and j<n2:
    if dp[i][j]==dp[i+1][j]:
        i+=1
    elif dp[i][j]==dp[i][j+1]:
        j+=1
    else:
        n+=s1[i]
        i+=1
        j+=1
print(n)