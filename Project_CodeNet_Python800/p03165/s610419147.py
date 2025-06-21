s = input()
t = input()
dp = [[0] * (len(s)+1) for _ in range(len(t)+1)]
for i in range(1, len(t)+1):
    ti = t[i-1]
    dp[i] = dp[i-1][:]
    for j in range(1, len(s)+1):
        if ti == s[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

ans = ''
sl = len(s)
tl = len(t)
while sl > 0 and tl > 0:
    if s[sl-1] == t[tl-1]:
        sl -= 1
        tl -= 1
        ans = s[sl] + ans
        continue
    if dp[tl][sl] == dp[tl][sl-1]:
        sl -= 1
    elif dp[tl][sl] == dp[tl-1][sl]:
        tl -= 1
print(ans)
