def lcs(str1, str2):
    """文字列str1, str2の最長共通部分列(Longest Common Subsequence, LCS)を求める。
    計算量 O(|str1||str2|)
    """
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # 復元
    res = ''
    i, j = len(str1), len(str2)
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            res = str1[i - 1] + res
            i -= 1
            j -= 1

    return res


s = input()
t = input()
print(lcs(s, t))