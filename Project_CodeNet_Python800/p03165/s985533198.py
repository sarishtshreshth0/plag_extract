def resolve():
    import sys
    def max2(a: int, b: int):
        """
        入力された2つの整数a,bの大きいほうを返す
        Parameters
        ----------
        a, b : int
            比較したい整数
        Returns
        -------
        a or b : int
            大きいほうの整数
        """
        if a >= b:
            return a
        else:
            return b
    
    readline = sys.stdin.readline
 
    s = readline()
    t = readline()
 
    # 配るDP
    # dp[i + 1][j + 1]はsのi文字目までとtのj文字目までのLCSの長さ
    # LCS=最長共通部分列問題
    dp = [[0] * (len(t) + 1) for _ in [0] * (len(s) + 1)]
 
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = max2(dp[i + 1][j + 1], dp[i][j] + 1)
            dp[i + 1][j + 1] = max2(dp[i + 1][j + 1], dp[i + 1][j])
            dp[i + 1][j + 1] = max2(dp[i + 1][j + 1], dp[i][j + 1])
 
    # LCSを求めたDPから部分文字列を復元
    res = []
    i, j = len(s), len(t)
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            res.append(s[i - 1])
            i -= 1
            j -= 1
    print(''.join(res[::-1]))
 
 
resolve()
