s=input() ; n=len(s)
t=input() ; m=len(t)

ans=[[0]*(n+1) for _ in range(m+1)]
dp=[[0]*(n+1) for _ in range(m+1)]

for i in range(1,m+1) :
    for j in range(1,n+1):
        if t[i-1] == s[j-1] :
            ans[i][j]='match' 
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=dp[i-1][j-1]
            ans[i][j]='lu'
            if dp[i-1][j]>=dp[i][j] :
                dp[i][j]=dp[i-1][j]
                ans[i][j]='u' 
            
            if dp[i][j-1]>=dp[i][j] :
                dp[i][j]=dp[i][j-1]
                ans[i][j]='l' 
for i in range(m+1):
    ans[i][0]='u'
for j in range(n+1):
    ans[0][j]='l'


answer=[]
i=m ; j=n 
while (i>=0 and j>=0):
    if ans[i][j]=='match' :
        answer.append(s[j-1])
        i-=1
        j-=1
    elif ans[i][j]=='l' :
        j-=1
    elif ans[i][j]=='lu':
        i-=1
        j-=1
    else:
        i-=1


answer.reverse()
print(''.join(answer))
