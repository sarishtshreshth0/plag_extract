import sys
from collections import deque
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()

n = ni()
print(2 * n if n % 2 != 0 else n)