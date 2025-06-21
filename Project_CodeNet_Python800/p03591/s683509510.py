# -*- coding: utf-8 -*-
"""
A - Snuke's favorite YAKINIKU
https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_a

"""
import sys


def solve(S):
    if S.startswith('YAKI'):
        return 'Yes'
    return 'No'


def main(args):
    S = input()
    ans = solve(S)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])