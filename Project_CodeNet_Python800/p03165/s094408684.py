# F - LCS
s = input()
t = input()

m = len(s)
n = len(t)

# dp[i][j]: s の i 文字目、 t の j 文字目までを比較したときの LSC の長さ
dp = [[0]*(n+1) for _ in range(m+1)]

# 初期条件
# 0 文字目 (i=0 or j=0) のとき LSC は 0
for i in range(m+1):
    dp[i][0] = 0
for j in range(n+1):
    dp[0][j] = 0

# s の v 文字目について
for v in range(1,m+1):
    # t の w 文字目について
    for w in range(1,n+1):
        # s の v 文字目と t の w 文字目が同じとき
        if s[v-1] == t[w-1]:
            dp[v][w] = dp[v-1][w-1] + 1
        # s の v 文字目と t の w 文字目が異なるとき
        else:
            dp[v][w] = max(dp[v-1][w],dp[v][w-1])

# 文字列を 「復元」
# DP テーブルの値を見ながら、今いるノード (i,j) がどのノードから更新されて来たのかを特定する

# 遡った文字を保持する配列
res = []

# DP テーブルの末端の index
i = m
j = n
while (i>0 and j>0):
    # (i-1, j) -> (i, j) と遷移していた場合 (s[i-1] != t[j-1]) 
    if (dp[i][j] == dp[i-1][j]):
        # DP の遷移を i について 1 遡る
        i -= 1
    else:
        # (i, j-1) -> (i, j) と遷移していた場合 (s[i-1] != t[j-1]) 
        if (dp[i][j] == dp[i][j-1]):
            # DP の遷移を j について 1 遡る
            j -= 1
        # (i-1, j-1) -> (i, j) と遷移していた場合 (s[i-1] == t[j-1]) 
        else:
            # s[i-1] == t[j-1] なので、res.append(t[j-1]) でも良い
            res.append(s[i-1])
            # DP の遷移を遡る
            i -= 1
            j -= 1
            
# res は逆方向から取得したので reverse する
ans = list(reversed(res))
print(''.join(ans))