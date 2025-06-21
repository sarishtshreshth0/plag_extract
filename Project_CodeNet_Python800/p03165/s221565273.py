s = input()
t = input()
slen = len(s)
tlen = len(t)
dp = [[0] * (tlen+1) for i in range(slen+1)]
for i in range(slen):
    for j in range(tlen):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
stlen = dp[slen][tlen]
ans = [0]*stlen
i = slen
j = tlen
while stlen > 0:
    if s[i-1] == t[j-1]:
        ans[stlen-1] = s[i-1]
        i -= 1
        j -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        j -= 1
    stlen = dp[i][j]
print(''.join(ans))