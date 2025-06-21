def main():
    s = input()
    t = input()

    len_s = len(s)
    len_t = len(t)

    # dp[i][j] = the maximum length of common part of s[:i] and t[:j]
    dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]
    for i in range(1, len_s + 1):
        for j in range(1, len_t + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    i, j = len_s, len_t
    ans = ''
    while dp[i][j] > 0:
        while dp[i-1][j] == dp[i][j]:
            i -= 1
        while dp[i][j-1] == dp[i][j]:
            j -= 1

        ans += s[i-1]
        i -= 1
        j -= 1

    print(ans[::-1])

main()
