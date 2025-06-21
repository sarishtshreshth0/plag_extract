s, t = input(), input()
ls, lt = len(s), len(t)
dp = [[0 for i in range(lt + 1)] for j in range(ls + 1)]
for i in range(ls):
    for j in range(lt):
        dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
ans = []
while ls > 0 or ls > 0:
    if dp[ls][lt] == dp[ls-1][lt]:
        ls -= 1
    elif dp[ls][lt] == dp[ls][lt-1]:
        lt -= 1
    else:
        ls -= 1
        lt -= 1
        ans.append(s[ls])
ans = reversed(ans)
print("".join(ans))