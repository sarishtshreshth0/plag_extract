s = input()
t = input()

sl = len(s)
tl = len(t)
dp = [[0 for i in range(tl+1)] for i in range(sl+1)]

#dp[i][j] sをi文字目、tをj文字目まで求めたときの最大の長さ

for i in range(1,sl+1):
    for j in range(1,tl+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

ansl = dp[sl][tl]
i = sl
j = tl
ans = [""]*ansl
while(ansl>0):
    if s[i-1] == t[j-1]:
        ans[ansl-1] = s[i-1]
        i -= 1
        j -= 1
        ansl -= 1
    elif dp[i][j]==dp[i-1][j]:
        i -= 1
    else:
        j -= 1

print("".join(ans))