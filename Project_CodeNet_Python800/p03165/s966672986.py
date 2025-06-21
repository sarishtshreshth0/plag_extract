import sys
sys.setrecursionlimit(1000000) # 再帰上限を増やす

def main():
    input = sys.stdin.readline  # 文字列に対してinputした場合は、rstripするのを忘れずに！
    S = input().rstrip()
    T = input().rstrip()

    # dp[i][j] = sのi番目とtのj番目まででえられる最長部分列の長さ
    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

    # 最長部分列の長さを探索
    for i, s in enumerate(S, 1):
        for j, t in enumerate(T, 1):
            # 一致するとき
            if s == t:
                # 一致する文字の一つ左側までの最大部分列に一致した文字を加える
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
            # 一致しない場合も、一つ手前の文字までの最大文字列を引き継ぐ
            dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

    # 最長だった場合の具体例を復元する
    i, j = len(S), len(T)
    ans = ""
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            ans = S[i-1] + ans
            i -= 1
            j -= 1
    print(ans)

if __name__ == '__main__':
    main()