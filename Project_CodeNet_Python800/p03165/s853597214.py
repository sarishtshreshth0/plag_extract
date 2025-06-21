s=input()
t=input()

dp=[[0 for _ in range(len(t)+1)] for _ in range(len(s))]

ans=[]
for i in range(len(s)):
    for j in range(len(t)):
        if s[i]==t[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])

x_index=len(t)-1
y_index=len(s)-1

if  dp[y_index][x_index]==0:
    print()
    exit()

while True:
    if t[x_index]==s[y_index]:
        ans.append(t[x_index])
        if dp[y_index][x_index]==1:
            break
        else:
            x_index-=1
            y_index-=1
            continue

    else:
        if dp[y_index][x_index]==dp[y_index][x_index-1]:
            x_index-=1
        else:
            y_index-=1


X=reversed(ans)
print(''.join(X))
