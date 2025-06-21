import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

A, B = map(int, input().split())
S = input()

if S.count("-") == 1 and S[A] == "-":
    print('Yes')
else:
    print('No')