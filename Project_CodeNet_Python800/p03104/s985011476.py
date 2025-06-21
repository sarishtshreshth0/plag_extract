import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def count(N):
    cnt = []
    r = 1
    while r < N:
        res = (N // (2 * r)) * r + max(N % (2 * r) - r, 0)
        cnt.append(res)
        r *= 2
    return cnt


def main():
    A, B = map(int, input().split())

    cnt_A = count(A)
    cnt_B = count(B + 1)

    cnt = [b for b in cnt_B]
    for i, a in enumerate(cnt_A):
        cnt[i] -= a

    res = 0
    for i, c in enumerate(cnt):
        if c % 2 != 0:
            res += 2 ** i

    print(res)


if __name__ == '__main__':
    main()
