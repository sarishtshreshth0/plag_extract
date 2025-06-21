s=input()
t=input()
l1=len(s)
l2=len(t)
dp=[[-1]*(l2+1) for i in range(l1+1)]   

for i in range(l1+1):
    for j in range(l2+1):
        if i==0 or j==0:
            dp[i][j]=0
            
        elif s[i-1]==t[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            

size=dp[l1][l2]
i,j=l1,l2
ans=[0]*size
while i>0 and j>0:
    if s[i-1]==t[j-1]:
        ans[size-1]=(s[i-1])
        i-=1
        j-=1
        size-=1
    elif dp[i-1][j]>dp[i][j-1]:
        i-=1
    else:
        j-=1
        
    
print(''.join(ans))

