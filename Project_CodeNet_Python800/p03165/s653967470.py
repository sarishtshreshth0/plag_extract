def LCS(s1,s2):
    l1, l2 = len(s1), len(s2)
    if l1 == 0 or l2 == 0:
        return ''
    
    dp = [[0 for i in range(l2+1)] for j in range(l1+1)]

    for i in range(l1):
        for j in range(l2):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            dp[i+1][j+1] = max(max(dp[i+1][j+1],dp[i][j+1]),dp[i+1][j])
    
    lcs_str = ''
    i,j = l1,l2
    while i>0 and j>0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            lcs_str += s[i-1]
            i -= 1
            j -= 1
    
    return lcs_str[::-1]

s = input()
t = input()
print(LCS(s,t))