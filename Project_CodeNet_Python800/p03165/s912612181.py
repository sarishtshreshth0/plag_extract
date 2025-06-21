def main():
    s = input()
    t = input()
    dp = [["" for _ in range(3010)] for _ in range(3010)]
    for i in range(len(s)):
        for j in range(len(t)):
            dp[i + 1][j + 1] = dp[i][j + 1] if len(dp[i][j + 1]) >= len(dp[i + 1][j]) else dp[i + 1][j]
            if s[i] == t[j] and len(dp[i][j]) + 1 > len(dp[i + 1][j + 1]):
                dp[i + 1][j + 1] = dp[i][j] + s[i]
    print(dp[len(s)][len(t)])


if __name__ == '__main__':
    main()
