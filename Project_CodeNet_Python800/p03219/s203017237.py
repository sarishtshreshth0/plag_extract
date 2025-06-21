import sys

stdin = sys.stdin

ni = lambda: int(ns())
ns = lambda: stdin.readline().rstrip()
na = lambda: list(map(int, stdin.readline().split()))

# code here
X, Y = na()

print(X+Y//2)
