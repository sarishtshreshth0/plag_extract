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
stack = [(len(S), len(T))]

while stack:
    x, y = stack.pop()
    if dp[x][y] == 0:
        break
    if x - 1 >= 0 and dp[x][y] == dp[x - 1][y]:
        stack.append((x - 1, y))
    elif y - 1 >= 0 and dp[x][y] == dp[x][y - 1]:
        stack.append((x, y - 1))
    else:
        res.append(S[x - 1])
        stack.append((x - 1, y - 1))

print(''.join(res[::-1]))