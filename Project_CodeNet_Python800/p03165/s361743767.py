import numpy as np
def resolve():
    s = np.array(list(input()))
    t = np.array(list(input()))

    dp = np.zeros([len(s) + 1, len(t) + 1], dtype=np.int64)

    match = s.reshape(-1, 1) == t.reshape(1, -1)

    for i in range(len(s)):
        dp[i + 1][1:] = np.maximum(dp[i][:-1] + match[i], dp[i][1:])
        dp[i + 1] = np.maximum.accumulate(dp[i + 1])

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