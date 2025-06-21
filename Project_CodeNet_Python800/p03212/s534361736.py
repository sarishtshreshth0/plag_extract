N = input()
l = len(N)

dp = [[[[0] * 2 for _ in range(8)]for _ in range(2)] for _ in range(l + 1)]
dp[0][False][0][False] = 1

for i in range(l):
    cur = int(N[i])

    for j in (3, 5, 7):
        if j == 3:
            s = 0
        elif j == 5:
            s = 1
        elif j == 7:
            s = 2

        for k in range(8):
            new = k | (1 << s)
            dp[i + 1][True][new][True] += dp[i][True][k][True]
            dp[i + 1][True][new][True] += dp[i][True][k][False]

        if j < cur:
            for k in range(8):
                new = k | (1 << s)
                dp[i + 1][True][new][True] += dp[i][False][k][True]
                dp[i + 1][True][new][True] += dp[i][False][k][False]

        if j == cur:
            for k in range(8):
                new = k | (1 << s)
                dp[i + 1][False][new][True] += dp[i][False][k][True]
                dp[i + 1][False][new][True] += dp[i][False][k][False]

    dp[i + 1][True][0][False] += dp[i][False][0][False]
    dp[i + 1][True][0][False] += dp[i][True][0][False]


print(dp[l][True][7][True] + dp[l][False][7][True])
