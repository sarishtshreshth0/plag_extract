def lcs(s, t):
    n = len(s)
    m = len(t)
    # dp[i][j] := 0-indexでsのi-1文字目までとtのj-1文字目までとのlcsの長さ
    # dp[0][0]は空文字を見ていると考えるからdp[0][0] = 0
    # dp[n][m] := sのn-1文字目まで（0-indexなのでsの末尾）とtのm-1文字目まで(0-indexなのでtの末尾)
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(m):
            # 0-indexでsのi文字目とtのj文字目が等しいなら斜めに移動する
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            # 異なるなら左または上のmaxをとる
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    res = ""
    while n != 0 and m != 0:  # どちらかが0になったら終わり，dp[0][*]及びdp[*][0]は必ず0なので
        # 上から遷移している場合，nをデクリメントしてよい
        if dp[n][m] == dp[n-1][m]:
            n -= 1
        # 左から遷移している場合，mをデクリメントしてよい
        elif dp[n][m] == dp[n][m-1]:
            m -= 1
        # 左でも上でもなく，左上からの遷移の場合，共通文字
        else:
            n -= 1
            m -= 1
            # 後ろから復元しているので以下のようにする
            res = s[n] + res
    return res


S = input()
T = input()
print(lcs(S, T))
