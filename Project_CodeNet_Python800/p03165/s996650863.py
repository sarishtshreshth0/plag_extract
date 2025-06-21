# F LCS

s = input()
t = input()

dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]

ans = []

for i,_s in enumerate(s):
    for j,_t in enumerate(t):
        dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        if _s == _t:
            dp[i+1][j+1] = max(dp[i][j]+1,dp[i+1][j+1])

i, j = len(s), len(t)

while i>0 and j>0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        ans.append(s[i-1])
        i -= 1
        j -= 1

print(*(list(reversed(ans))),sep="")