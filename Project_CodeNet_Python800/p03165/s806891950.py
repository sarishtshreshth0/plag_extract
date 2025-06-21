s = input()
t = input()
a = len(list(s))
b = len(list(t))
#dp[i][j] をsをi番目、ｔをj番目までの最長共通長
INF = float('inf')
dp = [[-INF for j in range(b+1)] for i in range(a+1)]
for i in range(a+1):
    dp[i][0] = 0
for j in range(b+1):
    dp[0][j] = 0
for i, x in enumerate(list(s)):
    for j, y in enumerate(list(t)):
        if x == y:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
#復元パート
ans = ''
while a > 0 and b >0:

    if dp[a][b] == dp[a-1][b]:
        a -= 1
    elif dp[a][b] == dp[a][b-1]:
        b -= 1
    else:
        ans = list(s)[a-1] + ans
        a -= 1
        b -= 1
print(ans)