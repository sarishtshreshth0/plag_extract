s= input()
t= input()
n=len(s)
m= len(t)
dp = [[0 for i in range(n+1)] for j in range(m+1)]
for j in range(1,n+1):
    for i in range(1,m+1):
        if s[j-1]==t[i-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
i =n
j=m
inde = dp[m][n]
an = [""] * (inde +1)
while i>0 and j>0:
    if s[i-1]==t[j-1]:
        an[inde-1]=s[i-1]
        i-=1
        j-=1
        inde-=1
    elif dp[j-1][i]>dp[j][i-1]:
        j-=1
    else:

        i-=1
print(''.join(an))
