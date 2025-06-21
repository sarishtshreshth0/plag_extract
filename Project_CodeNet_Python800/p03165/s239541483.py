s = input()
t = input()

S, T = len(s), len(t)
dp = [[0]*(T+1) for _ in range(S+1)]
prev = [[(-1,-1)]*(T+1) for _ in range(S+1)]

for i in range(S):
    for j in range(T): 
        r = max(dp[i][j-1], dp[i-1][j])
        p = (i, j-1) if r == dp[i][j-1] else (i-1, j)
        if s[i] == t[j]:
            r = max(dp[i-1][j-1] + 1, r) 
            p = (i-1, j-1) if r == dp[i-1][j-1] + 1 else p
        dp[i][j] = r
        prev[i][j] = p


ans = ''
i, j = S - 1, T - 1
while i >= 0 and j >= 0:
    if prev[i][j] == (i-1, j-1):
        ans += s[i]
    i, j = prev[i][j]

print(ans[::-1])