import sys

X = int(sys.stdin.readline())

a = X // 500
b = (X - a * 500) // 5
print(a * 1000 + b * 5)