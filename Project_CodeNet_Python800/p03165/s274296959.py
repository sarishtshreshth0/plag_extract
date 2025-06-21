def lcs(s,t):
    m = len(s)
    n = len(t)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = 1+ dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    
    
    substr = ""
    i,j = m,n
    while i>0 and j>0:
        if s[i-1] == t[j-1]:
            substr+=s[i-1]
            i-=1
            j-=1
        elif dp[i][j-1]>dp[i-1][j]:
            j-=1
        else:
            i-=1
    return substr[::-1]
    
    

# s = "abracadabra"
# t = "avadakedavra"
# s = "axyb"
# t = "abyxb"
s = input()
t = input()
print(lcs(s,t))