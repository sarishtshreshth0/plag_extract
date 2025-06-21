def main():
    s = input()
    t = input()

    len_s = len(s)
    len_t = len(t)

    DP = [[0] * (len_t + 1) for _ in range(len_s + 1)]

    for i in range(len_s):
        for j in range(len_t):
            if s[i] == t[j]:
                DP[i + 1][j + 1] = DP[i][j] + 1
            else:
                DP[i + 1][j + 1] = max(DP[i + 1][j], DP[i][j + 1])

    ans = ""
    i = len_s
    j = len_t
    while DP[i][j]:
        if s[i - 1] == t[j - 1]:
            ans += s[i - 1]
            i -= 1
            j -= 1
        else:
            if DP[i - 1][j] > DP[i][j -1]:
                i -= 1
            else:
                j -= 1

    print(ans[::-1])


if __name__ == '__main__':
    main()

exit()