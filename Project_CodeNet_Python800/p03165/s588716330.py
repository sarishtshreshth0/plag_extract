s = input()
t = input()
lenS = len(s)
lenT = len(t)
dp = []
for i in range(lenS+1):
    dp.append([0]*(lenT+1))
for i in range(1,lenS+1):
    for j in range(1,lenT+1):
        if s[i-1]==t[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
ans=""
i=lenS
j=lenT
while i>0 and j>0:
    if dp[i][j]==dp[i-1][j]:
        i-=1
    elif dp[i][j]==dp[i][j-1]:
        j-=1
    else:
        ans+=s[i-1]
        i-=1
        j-=1
print(ans[::-1])