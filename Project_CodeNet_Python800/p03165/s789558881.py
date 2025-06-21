def solve():
    s = input()
    t = input()
    s_size = len(s)
    t_size = len(t)
    dp = [[0 for i in range(s_size+1)] for j in range(t_size+1)]
    for i in range(1, t_size+1):
        for j in range(1, s_size+1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    ans = ""
    i, j = t_size, s_size
    while i > 0 and j > 0:
        if dp[i][j] == dp[i][j-1]:
            j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            ans = t[i-1] + ans
            i -= 1
            j -= 1
    print(ans)
solve()