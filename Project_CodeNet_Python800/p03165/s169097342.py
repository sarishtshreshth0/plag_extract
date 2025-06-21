S = input()
T = input()
N = len(S)
M = len(T)
#dp[i][j] -> Sのi文字目、Tのj文字目までみるとき、最長共通部分列の長さ
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    s = S[i-1]
    for j in range(1,M+1):
        t = T[j-1]
        if s == t:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
ans = []
while N and M:
    if dp[N][M] > max(dp[N-1][M],dp[N][M-1]):
        ans.append(S[N-1])
        N -= 1
        M -= 1
    elif dp[N][M] == dp[N-1][M]:
        N -= 1
    else:
        M -= 1

ans = ans[::-1]

ans = "".join(ans)
print(ans)