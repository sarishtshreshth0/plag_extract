import sys
input = lambda: sys.stdin.readline().rstrip()

X, Y = map(int, input().split())

print(X + Y//2)