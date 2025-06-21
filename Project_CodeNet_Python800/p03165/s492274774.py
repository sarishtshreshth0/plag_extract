def main():
    s = input()
    t = input()

    """
    dp[i][j] := s[1] ... s[i] と t[1] ... t[j] に対するLCSの長さ
    
    s[i+1] == t[i+1]のとき、dp[i+1][j+1]は dp[i][j]+1, dp[i+1][j], dp[i][j+1]のいずれか  
    dp[i+1][j+1] = max(dp[i][j] + 1, dp[i+1][j], dp[i][j+1])

    それ以外の時
    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    """

    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j], dp[i][j + 1])
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    ans = ""
    x = len(s)
    y = len(t)
    while x >= 1 and y >= 1:
        if dp[x][y] == dp[x - 1][y]:
            x -= 1
        elif dp[x][y] == dp[x][y - 1]:
            y -= 1
        else:
            x -= 1
            y -= 1
            ans = s[x] + ans

    print(ans)


if __name__ == "__main__":
    main()
