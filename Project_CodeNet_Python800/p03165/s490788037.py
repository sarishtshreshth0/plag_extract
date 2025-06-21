

INF = float('inf')


def tc():
    s = input()
    t = input()
    n, m = len(s), len(t)

    # dp[i][j] = LCS so far up to pos i in s and pos j in t
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:  # if chars are the same, use them both
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = n, m
    ans = ''
    while dp[i][j]:
        me = dp[i][j]
        l = dp[i][j - 1]
        u = dp[i - 1][j]
        d = dp[i - 1][j - 1]
        if d > l and d > u:
            ans += s[i - 1]
            i -= 1
            j -= 1
        elif d == l and d == u:
            if d < me:
                ans += s[i - 1]
                i -= 1
                j -= 1
            else:
                i -= 1
        elif l >= u:
            j -= 1
        elif u > l:
            i -= 1

    print(''.join(reversed(ans)))


tc()
