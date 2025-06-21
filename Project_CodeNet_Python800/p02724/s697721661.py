import sys
input = sys.stdin.readline
X = int(input())
res = X // 500 * 1000
print(res + (X % 500) // 5 * 5)