# メイン関数
def main():
    # 入力データ
    s = input()
    t = input()

    # dpテーブルの作成
    dp = [[0] * (len(t)+1) for i in range(len(s)+1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    # 部分列の復元
    ans = ''
    i = len(s)
    j = len(t)
    while i != 0 and j != 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            i -= 1
            j -= 1
            ans = s[i] + ans

    # 解答の出力
    print(ans)
    return


# 実行
if __name__ == '__main__':
    main()
