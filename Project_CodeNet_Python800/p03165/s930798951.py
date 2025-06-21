s = input()
t = input()

dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(t)):
        if s[i]==t[j]: #末尾が共通なら使った方がいい
            dp[i+1][j+1] = dp[i][j]+1
        else: #そうでないなら片方を削除
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
            
#復元
x = len(s)
y = len(t)
res = ''
while(dp[x][y]):
    if dp[x][y-1]==dp[x][y]: #行けるだけ左に
        y -= 1
    elif dp[x-1][y]==dp[x][y]: #行けるだけ上に
        x -= 1
    else:
        res = s[x-1] + res
        x -= 1
        y -= 1

print(res)