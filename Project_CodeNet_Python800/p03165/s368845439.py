s = input()
t = input()

def LCS(X,Y):
    XL = len(X)
    YL = len(Y)
    dp = [[0 for j in range(YL+1)] for i in range(XL+1)]
    for i in range(XL):
        for j in range(YL):
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    # 以下復元
    idx = dp[XL][YL]-1
    S = [0]*(idx+1)
    i,j = i+1,j+1
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            i,j = i-1,j-1
            S[idx] = X[i]
            idx -= 1
    return S

print(''.join(LCS(s,t)))
