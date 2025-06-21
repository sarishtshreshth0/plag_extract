import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def input(): return sys.stdin.readline().rstrip()

A, B = map(int, input().split())
print('Yes' if any(A * B * C % 2 == 1 for C in range(1, 4)) else 'No')