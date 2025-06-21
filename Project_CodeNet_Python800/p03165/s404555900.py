S = input()
T = input()

dp = [[0 for j in range(len(T) + 1)] for i in range(len(S) + 1)]

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j], dp[i][j + 1])
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

res = []

i = len(S)
j = len(T)

while i and j:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        res.append(S[i - 1])
        i -= 1
        j -= 1

print(''.join(res[::-1]))