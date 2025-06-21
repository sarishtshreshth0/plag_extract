a=input()
b=input()
dp=[[0 for i in range(len(a)+1)] for j in range(len(b)+1)]
for i in range(1,len(b)+1):
  for j in range(1,len(a)+1):
    if a[j-1]==b[i-1]:
      dp[i][j]=dp[i-1][j-1]+1
    else:
      dp[i][j]=max(dp[i-1][j],dp[i][j-1])

res=''

j=len(a)
i=len(b)
while j>0 and i>0:
 
    if dp[i][j]==dp[i-1][j]:
        i-=1
  
    elif dp[i][j]==dp[i][j-1]:
        j-=1
    elif dp[i][j]==dp[i-1][j-1]+1:

        res+=a[j-1]
        i-=1
        j-=1
    
print(res[::-1])
        
