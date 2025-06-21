S = input()
T = input()
lenS = len(S)
lenT = len(T)
dp = [[0]*(lenT+1) for _ in range(lenS+1)]
for i in range(1,lenS+1):
    for j in range(1,lenT+1):
        if S[i-1]==T[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
ans = []
while lenS!=0 and lenT!=0:
    if dp[lenS][lenT]==dp[lenS-1][lenT]:
        lenS-=1
    elif dp[lenS][lenT]==dp[lenS][lenT-1]:
        lenT-=1
    else:
        ans.append(S[lenS-1])
        lenS-=1
        lenT-=1
ans = ans[::-1]
print("".join(ans))