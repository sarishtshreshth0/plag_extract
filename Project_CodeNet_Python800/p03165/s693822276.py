from collections import deque
s1=input()
s2=input()
n=len(s1)
m=len(s2)
dp=[[0]*(m+1) for i in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if(i==0 or j==0):
            dp[i][j]=0
        else:
            if(s1[i-1]==s2[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
x=n
y=m
ans=""
while x>0 and y>0:
    if(s1[x-1]==s2[y-1]):
        ans+=s1[x-1]
        x-=1
        y-=1
    else:
        if(dp[x-1][y]>dp[x][y-1]):
            x-=1
        else:
            y-=1
            
'''
if(x==0):
    for i in range(y,-1,-1):
        if(s1[x]==s2[i]):
            ans+=s1[x]
            break
elif(y==0):
    for i in range(x,0,-1):
        if(s1[i]==s2[y]):
            ans+=s1[i]
            break
'''
'''
aabaaa
ababba
'''
print(ans[::-1])