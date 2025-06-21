# python3だとTLE,pypy3だとAC
def main():
    s = input()
    t = input()
    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i, cs in enumerate(s, start=1):
        for j, ct in enumerate(t, start=1):
            if cs == ct:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    ans = ""
    i = len(s)
    j = len(t)
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            i -= 1
            j -= 1
            ans = s[i] + ans

    print(ans)


if __name__ == "__main__":
    main()
