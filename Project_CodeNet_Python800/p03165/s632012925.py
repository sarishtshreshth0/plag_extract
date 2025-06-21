s = input()
t = input()

m = len(s)
n = len(t)

dp = [[None] * (n+1) for i in range(m+1)]

for i in range(m+1):
    for j in range(n+1):

        if i == 0 or j == 0:
            dp[i][j] = 0

        elif s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])



final = dp[m][n]

lcs = [""] * (final + 1)
lcs[final] = ""

i = m
j = n

while i > 0 and j > 0:
    if s[i-1] == t[j-1]:
        lcs[final-1] = s[i-1]
        i -= 1
        j -= 1
        final -= 1

    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1


print("".join(lcs))
