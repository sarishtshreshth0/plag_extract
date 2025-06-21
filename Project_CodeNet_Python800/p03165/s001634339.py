s = input()
t = input()
len_s = len(s)
len_t = len(t)

# dp[i][j] = sのi-1文字目,tのj-1文字目まででの最長共通部分列の長さ
dp = [[0]*(len_t+1) for i in range(len_s+1)]
# 遷移記録用（0,1が両方-1ならその文字を追加する）
prevs = [[0]*(len_t+1) for i in range(len_s+1)]
prevt = [[0]*(len_t+1) for i in range(len_s+1)]
for i in range(len_s+1) :
    for j in range(len_t+1) :
        # どちらかが空文字列の場合
        if i == 0 or j == 0 :
            dp[i][j] = 0
            continue
        # i-1文字目とj-1文字目が一致する場合
        if s[i-1] == t[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
            prevs[i][j] = -1
            prevt[i][j] = -1
        # 一致しない場合
        else : 
            if dp[i-1][j] >= dp[i][j-1] :
                if dp[i-1][j] > dp[i][j] :
                    dp[i][j] = dp[i-1][j]
                    prevs[i][j] = -1
            else :
                if dp[i][j-1] > dp[i][j] :
                    dp[i][j] = dp[i][j-1]
                    prevt[i][j] = -1

ans = 0
si = len_s
ti = len_t
ans = ['' for i in range(dp[len_s][len_t])]
index = dp[len_s][len_t] - 1
# 遷移をたどっていく
for i in range(10**18) :
    if prevs[si][ti] == -1 and prevt[si][ti] == -1 :
        ans[index] = s[si-1]
        index -= 1
    st = si ; tt = ti
    si += prevs[st][tt] ; ti += prevt[st][tt]
    if si == st and ti == tt :
        break

print(*ans, sep='')