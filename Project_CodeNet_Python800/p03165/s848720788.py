def edu_dp_f_lcs():
    s = input()
    t = input()
    slen = len(s)
    tlen = len(t)
    dp = [[0] * (tlen+1) for _ in range(slen+1)]
    for i in range(slen):
        for j in range(tlen):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    l = dp[slen][tlen]
    i = slen-1
    j = tlen-1
    ans = ''
    while l > 0:
        if s[i] == t[j]:
            ans = s[i]+ans
            j -= 1
            i -= 1
            l -= 1
        elif dp[i+1][j+1] == dp[i][j+1]:
            i-=1
        else:
            j-=1
    print(ans)

edu_dp_f_lcs()