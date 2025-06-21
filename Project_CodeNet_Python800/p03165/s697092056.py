def resolve():
    s = input()
    t = input()

    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

    for i in range(len(s)):
        for j in range(len(t)):
            match = s[i] == t[j]
            dp[i + 1][j + 1] = max(dp[i][j] + match , dp[i + 1][j + 1])
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i + 1][j + 1])
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j + 1])

    res = ''
    i = len(s)
    j = len(t)

    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        elif dp[i][j] == dp[i - 1][j - 1] + 1:
            res = s[i - 1] + res
            i -= 1
            j -= 1

    print(res)
resolve()