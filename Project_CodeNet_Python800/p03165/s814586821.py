s = input()
t = input()

dp = [[0] * (len(t) + 1) for i in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

nums = len(s)
numt = len(t)
d = dp[nums][numt]
ans = ""

while True:
    if d == 0:
        break
    if dp[nums][numt - 1] == d:
        numt -= 1
    elif dp[nums - 1][numt] == d:
        nums -= 1
    else:
        ans += s[nums - 1]
        nums -= 1
        numt -= 1
        d -= 1

print(ans[::-1])
