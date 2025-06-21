n=input()
m=input()
x=len(n)
 
y=len(m)
 
dp=[[0 for i in range(y+1)] for j in range(x+1)]
#print(len(dp),len(dp[0]))
for i in range(0,x+1):
  for j in range(0,y+1):
    if(i==0 or j==0):
      dp[i][j]=0
    elif n[i-1]==m[j-1]:
      dp[i][j]=1+dp[i-1][j-1]
    else:
      dp[i][j]=max(dp[i-1][j],dp[i][j-1])
 
i=x
j=y
ans=""
 
while i>0 and j>0:
    if(n[i-1]==m[j-1]):
        ans=ans+n[i-1]
        #print(n[i-1],1)
        i=i-1
        j=j-1
    else:
        mx=max(dp[i-1][j],dp[i][j-1])
        if mx==dp[i-1][j]:
            i=i-1
        else:
            j=j-1
print(ans[::-1])
        
