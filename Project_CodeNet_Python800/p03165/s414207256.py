X = input()
Y = input()
dp = [[0 for j in range(len(Y)+1)] for i in range(len(X)+1)]
fxy = [[(0, 0) for j in range(len(Y)+1)] for i in range(len(X)+1)]
for i in range(len(X)):
    for j in range(len(Y)):
        if X[i] == Y[j]:
            dp[i+1][j+1] = dp[i][j] + 1
            fxy[i+1][j+1] = (i, j)
        elif dp[i+1][j] >= dp[i][j+1]:
            dp[i+1][j+1] = dp[i+1][j]
            fxy[i+1][j+1] = (i+1, j)
        else:
            dp[i+1][j+1] = dp[i][j+1]
            fxy[i+1][j+1] = (i, j+1)
ans = ''
px, py = -1, -1
while not(px == py == 0):
    cx, cy = fxy[px][py]
    if dp[px][py] != dp[cx][cy]:
        ans += X[cx]
    px, py = cx, cy
print(ans[::-1])
# for i in range(len(X)+1):
#     print(dp[i])
# for i in range(len(X)+1):
#     print(fxy[i])
