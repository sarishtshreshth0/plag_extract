s = input()
t = input()
ls, lt = len(s), len(t)

# DP
dp = [[0 for _ in range(lt + 1)] for j in range(ls + 1)]

for i in range(ls):
    for j in range(lt):
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)

# 復元
ans = ""
while ls > 0 and lt > 0:
    if dp[ls][lt] == dp[ls-1][lt]:
        ls -= 1
    elif dp[ls][lt] == dp[ls][lt-1]:
        lt -= 1
    elif dp[ls][lt] == dp[ls-1][lt-1] + 1:
        ans += s[ls-1]
        ls -= 1
        lt -= 1
print(ans[::-1])