# LCS(Longest common subsequence)
s = input()
t = input()

def lcs(str1, str2):
    len1, len2 = len(str1), len(str2)
    lcs_dp = [[0]*(len2+1) for i in range(len1+1)]
    for i in range(len1-1, -1, -1):
        for j in range(len2-1, -1, -1):
            r = max(lcs_dp[i+1][j], lcs_dp[i][j+1])
            if str1[i] == str2[j]:
                r = max(r, lcs_dp[i+1][j+1]+1)
            lcs_dp[i][j] = r
    res = []
    i, j = 0, 0
    while i < len1 and j < len2:
        if str1[i] == str2[j]:
            res.append(str1[i])
            i += 1; j += 1
        elif lcs_dp[i][j] == lcs_dp[i+1][j]:
            i += 1
        elif lcs_dp[i][j] == lcs_dp[i][j+1]:
            j += 1
    return ''.join(res)

print(lcs(s, t))