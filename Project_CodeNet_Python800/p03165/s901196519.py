#!python3

# input
s = input()
t = input()


def main():
    sn, tn = len(s), len(t)
    dp = [[0] * (tn + 1) for _ in range(sn + 1)]
    w = [[None] * (tn + 1) for _ in range(sn + 1)]
    for i in range(1, sn + 1):
        for j in range(1, tn + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                w[i][j] = s[i - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    ans = []
    i, j = sn, tn
    while i != 0 and j != 0:
        if s[i - 1] == t[j - 1]:
            ans.append(w[i][j])
            i, j = i - 1, j - 1
        else:
            if dp[i][j - 1] < dp[i - 1][j]:
                i -= 1
            else:
                j -= 1
    print("".join(ans[::-1]))


if __name__ == "__main__":
    main()
