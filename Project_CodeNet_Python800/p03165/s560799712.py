from sys import stdin


# 最大化問題
def chmax(a,b):
    if a < b: return b
    else: return a


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    s =     _in[0]   # type:str
    t =     _in[1]   # type:str
    S, T = len(s), len(t)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    dp = [[0] * (T+1) for _ in range(S+1)]  # 最大化問題
    # dp[i+1][j+1]:=sのi文字目までとtのj文字目までのLCSの長さ
    dp[0][0] = 0  # 初期条件

    # 配るDP
    for i,_s in enumerate(s):
        for j,_t in enumerate(t):
            if _s == _t:
                dp[i+1][j+1] = chmax(dp[i+1][j+1],dp[i][j]+1)
            dp[i+1][j+1] = chmax(dp[i+1][j+1],dp[i+1][j])
            dp[i+1][j+1] = chmax(dp[i+1][j+1],dp[i][j+1])

    ans = ''
    i, j = S, T
    while (i>0 and j>0):
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            ans = s[i-1] + ans
            i -= 1
            j -= 1
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(ans)
