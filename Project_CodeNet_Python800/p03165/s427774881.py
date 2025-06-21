import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    txt=""
    dp = [[0] * (lt + 1) for _ in range(ls + 1)]
    for i in range(1, ls + 1):
        for j in range(1, lt + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    while lt != 0 and ls != 0:
        if dp[ls][lt] == dp[ls - 1][lt]:
            ls -= 1
        elif dp[ls][lt] == dp[ls][lt - 1]:
            lt -= 1
        else:
            ls -= 1
            lt -= 1
            txt = txt +s[ls]

    print(txt[::-1])


if __name__ == "__main__":
    main()
