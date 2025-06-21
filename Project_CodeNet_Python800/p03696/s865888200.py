import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    S = input()

    T = []
    cnt = 0
    for s in S:
        if s == ')' and cnt == 0:
            T = ['('] + T + [')']
        elif s == ')' and cnt > 0:
            T = T + [')']
            cnt -= 1
        else:
            T = T + ['(']
            cnt += 1

    T = ['(' if t == ')' else ')' for t in T]
    new_S = T[::-1]

    T = []
    cnt = 0
    for s in new_S:
        if s == ')' and cnt == 0:
            T = ['('] + T + [')']
        elif s == ')' and cnt > 0:
            T = T + [')']
            cnt -= 1
        else:
            T = T + ['(']
            cnt += 1

    T = ['(' if t == ')' else ')' for t in T]
    T = T[::-1]
    print(''.join(T))


if __name__ == '__main__':
    main()
