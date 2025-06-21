import sys
from fractions import gcd


sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    # i番目から左の全ての要素のGCD
    gcd_from_left = [None] * N
    gcd_from_left[0] = A[0]
    # i番目から右の全ての要素のGCD
    gcd_from_right = [None] * N
    gcd_from_right[-1] = A[-1]

    for i in range(1, N):
        gcd_from_left[i] = gcd(A[i], gcd_from_left[i - 1])

    for i in range(N - 2, -1, -1):
        gcd_from_right[i] = gcd(A[i], gcd_from_right[i + 1])

    gcd_from_right.sort()

    # 要素iを取り除いたときの最大公約数
    ans = max(gcd_from_left[-2], gcd_from_right[1])
    for i in range(1, N - 1):
        tmp = gcd(gcd_from_right[i + 1], gcd_from_left[i - 1])
        if tmp > ans:
            ans = tmp

    print(ans)


if __name__ == "__main__":
    main()
