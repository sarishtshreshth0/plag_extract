import sys

stdin = sys.stdin

ni = lambda: int(ns())
ns = lambda: stdin.readline().rstrip()
na = lambda: list(map(int, stdin.readline().split()))

# code here
a, b = na()

if a == 2 or b == 2:
    print('No')
else:
    print('Yes')
