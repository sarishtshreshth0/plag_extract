# -*- coding: utf-8 -*-
"""
A - Discount Fare
https://atcoder.jp/contests/abc113/tasks/abc113_a

"""
import sys


def solve(X, Y):
    return X + Y//2


def main(args):
    X, Y = map(int, input().split())
    ans = solve(X, Y)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
