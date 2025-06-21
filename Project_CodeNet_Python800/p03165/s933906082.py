# educational DP contest F

X = input()
Y = input()
x = len(X)
y = len(Y)

dp = [[0 for _ in range(y + 1)] for _ in range(x + 1)]
for i in range(x):
    for j in range(y):
        if X[i] == Y[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

# print(dp[x][y])

ans = ''
while x > 0 and y > 0:
    if dp[x][y] == dp[x][y - 1]:
        y -= 1
    elif dp[x][y] == dp[x - 1][y]:
        x -= 1
    else:
        ans += X[x - 1]
        x -= 1
        y -= 1

print(ans[::-1])
