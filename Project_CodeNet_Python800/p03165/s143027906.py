a = input()
b = input()
n = len(a)
m = len(b)
dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

lim = dp[-1][-1]

i = n
j = m
ans = [None] * (lim)
while i > 0 and j > 0:

    if a[i - 1] == b[j - 1]:
        ans[lim-1] = a[i - 1]
        i -= 1
        j -= 1
        lim -= 1

    else:
        if dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
if ans:
    print("".join(ans))
else:
    print(' ')