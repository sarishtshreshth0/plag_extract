# -*- coding: utf-8 -*-
"""
A - On the Way
https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_a

"""
import sys


def solve(A, B, C):
    if A < C < B:
        return 'Yes'
    elif A > C > B:
        return 'Yes'
    return 'No'


def main(args):
    A, B, C = map(int, input().split())
    ans = solve(A, B, C)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
