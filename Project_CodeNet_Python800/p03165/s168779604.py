# LCS
s = input()
t = input()
ls, lt = len(s), len(t)
dp = [[0 for i in range(ls + 1)] for j in range(lt + 1)]
prev = [[0 for i in range(ls + 1)] for j in range(lt + 1)]
for i in range(lt):
    for j in range(ls):
        dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        if t[i] == s[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
# 復元
ans = []
x = lt
y = ls
while x > 0 and y > 0:
    if dp[x][y] == dp[x-1][y]:
        x -= 1
    elif dp[x][y] == dp[x][y-1]:
        y -= 1
    else:
        x -= 1
        y -= 1
        ans.append(t[x])
ans = reversed(ans)
print("".join(ans))