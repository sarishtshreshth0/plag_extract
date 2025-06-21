s=list(input())
t=list(input())
dp=[[0]*(3030) for j in range(3030)]

for i in range(len(s)):
    for j in range(len(t)):
        if s[i]==t[j]:
             dp[i+1][j+1] = dp[i][j]+1


        else:
            dp[i+1][j+1] =max(dp[i][j+1],dp[i+1][j])

#print(dp[len(s)][len(t)])
answer=[]
i,j=len(s),len(t)
d=dp[i-1][j-1]
while i>=0 and j>=0:

    if dp[i-1][j]==dp[i][j]:
        i-=1
    elif dp[i][j-1]==dp[i][j]:
        j-=1
    else:
        answer.append(s[i - 1])
        i -= 1
        j -= 1
print("".join(reversed(answer)))