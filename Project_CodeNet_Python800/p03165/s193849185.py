def main():
    import sys
    input = sys.stdin.readline

    S = list(input().rsplit()[0])
    T = list(input().rsplit()[0])

    NS = len(S)
    NT = len(T)

    # dp[i+1][j+1]: Sのi文字目と，Tのj文字目までのLCS
    dp = [[0]*(NT+1) for _ in range(NS+1)]

    for i in range(NS):
        for j in range(NT):
            if S[i] == T[j]:
                # dp[i+1][j+1] = max(dp[i][j] + 1, dp[i+1][j], dp[i][j+1])
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    ans = ''
    i = NS
    j = NT
    while i > 0 and j > 0:
        if dp[i][j] == dp[i][j-1]:
            j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            ans = S[i-1]+ans
            j -= 1
            i -= 1

    print(ans)


if __name__ == "__main__":
    main()
