from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float("inf")


def main():
    H, W = map(int, input().split())

    if H == 1 or W == 1:
        print(1)
    else:
        print((H * W + 1) // 2)


if __name__ == '__main__':
    main()