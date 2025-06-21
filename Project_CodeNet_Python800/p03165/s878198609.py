s = input()
t = input()
length_s = len(s)
length_t = len(t)

# dp[i+1][j+1] --> sのi文字目までとtのj文字までのLCSの長さ
dp = [[0] * 3005 for _ in range(3005)]

# DPループ
# LCSの長さを記録
for i in range(length_s):
    for j in range(length_t):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1])

# DPテーブルからLCSの文字列を復元
res = ""
i = length_s
j = length_t
while i > 0 and j > 0:
    # (i-1, j) -> (i, j)と更新されていた場合
    if dp[i][j] == dp[i-1][j]:
        i -= 1 # DPの遷移を遡る
    
    # (i, j-1) -> (i, j)と更新されていた場合
    elif dp[i][j] == dp[i][j-1]:
        j -= 1 # DPの遷移を遡る

    # (i-1, j-) -> (i, j)と更新されていた場合
    else:
        # この時s[i-1] == t[j-1]なのでt[i-1] + resでも可
        res = s[i-1] + res
        i -= 1
        j -= 1

print(res)
