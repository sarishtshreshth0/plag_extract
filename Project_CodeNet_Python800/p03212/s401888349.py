def digit(N, M):
    def f(j,k):
        if k==3: res = 1
        elif k==5: res = 2
        elif k==7: res = 4
        return j|res

    L = len(N)
    dp = [[[0] * M for i in range(L + 1)] for j in range(2)]

    dp[0][0][0] = 1
    for i in range(1,L):
        dp[1][i][0] = 1
    for i in range(L):
        for j in range(M):
            for k in [3,5,7]:
                if k < int(N[i]):
                    dp[1][i+1][f(j, k)] += dp[0][i][j] + dp[1][i][j]
                elif k == int(N[i]):
                    dp[0][i+1][f(j, k)] += dp[0][i][j]
                    dp[1][i+1][f(j, k)] += dp[1][i][j]
                else:
                    dp[1][i+1][f(j, k)] += dp[1][i][j]
    return dp[0][L][K] + dp[1][L][K]

###########################################################################

N = input().rstrip()
K = 7
M = K + 1                               # 状態数
print(digit(N, M))

