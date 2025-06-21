a=input()
b=input()
dp=[[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            dp[i+1][j+1]=dp[i][j]+1
        else:
            dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
s1=a
s2=b

# print(dp[len(s1)][len(s2)])
x=len(a)
y=len(b)
res=''
# print(dp[len(a)][len(b)])
while x>0 and y>0:
    if a[x-1]==b[y-1]:
        res+=a[x-1]
        x-=1
        y-=1
    elif dp[x][y]==dp[x-1][y]:
        x-=1
    elif dp[x][y]==dp[x][y-1]:
        y-=1
print(res[::-1])
        
    
