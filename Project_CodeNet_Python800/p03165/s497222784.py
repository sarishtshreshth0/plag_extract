s = input()
t = input()
ls = len(s)
lt = len(t)
dp = [[0 for _ in range(ls + 1)] for _ in range(lt + 1)]
for i in range(1, lt+1):
    for j in range(1, ls+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if s[j-1] == t[i-1]:
            dp[i][j] = max(dp[i-1][j-1] + 1, dp[i][j-1])
ans = ''
# print(*dp, sep='\n')
while ls > 0 and lt > 0:
    if dp[lt][ls] == dp[lt-1][ls]:
        lt -= 1
    elif dp[lt][ls] == dp[lt][ls-1]:
        ls -= 1
    else:
        ans += s[ls-1]
        lt -= 1
        ls -= 1

print(ans[::-1])