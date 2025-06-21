s = str(input())
t = str(input())
ls = len(s) + 1
lt = len(t) + 1

dp = [[0] * ls for _ in range(lt)]
for i in range(1, ls):
    for j in range(1, lt):
        if s[i-1] == t[j-1]:
            dp[j][i] = dp[j-1][i-1] + 1
        else:
            dp[j][i] = max(dp[j][i-1],dp[j-1][i])

revlst = []

lt -= 1
ls -= 1
while dp[lt][ls] != 0:
    while dp[lt][ls] == dp[lt-1][ls]:
        lt -= 1
    while dp[lt][ls] == dp[lt][ls-1]:
        ls -= 1
    revlst.append(lt)
    lt -= 1
    ls -= 1

ans = ''.join([t[_-1] for _ in reversed(revlst)])
print(ans)