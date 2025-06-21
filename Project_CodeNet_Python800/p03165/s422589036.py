def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)

    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    # 復元パート 昔のコピペ
    res = ""
    while N > 0 and M > 0:
        if dp[N][M] == dp[N-1][M]:
            N -= 1
        elif dp[N][M] == dp[N][M-1]:
            M -= 1
        else:
            res = S[N-1] + res
            N -= 1
            M -= 1
    print(res)


if __name__ == '__main__':
    main()
