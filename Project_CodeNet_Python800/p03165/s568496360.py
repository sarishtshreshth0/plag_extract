S = input()
T = input()
s = len(S)
t = len(T)
dp = [[0] * (t + 1) for _ in range(s + 1)]
for i in range(s):
    for j in range(t):
        if S[i] == T[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1])
A = ''
i = s
j = t
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        A = S[i - 1] + A
        i -= 1
        j -= 1
print(A)