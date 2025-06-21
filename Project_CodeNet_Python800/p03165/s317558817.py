s = input()
t = input()
dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

hassame = False
for i, s_ in enumerate(s):
    if hassame or s_ == t[0]: dp[i+1][1]=1; hassame=True
hassame = False
for i, t_ in enumerate(t):
    if hassame or t_ == s[0]: dp[1][i+1]=1; hassame=True

lcs = 0
for i, s_ in enumerate(s):
    if i==0: continue
    for j, t_ in enumerate(t):
        if j==0: continue
        if s_!=t_:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        else:
            dp[i+1][j+1] = dp[i][j]+1
        lcs = max(lcs, dp[i+1][j+1])

ans = ''
i, j = len(s), len(t)
while 0<i and 0<j:
        if s[i-1] == t[j-1]: ans+=s[i-1]; i-=1; j-=1
        else:
            if dp[i-1][j] > dp[i][j-1]: i-=1
            else: j-=1
print(ans[::-1])


for i in range(len(s)):
    dp+=s[i]