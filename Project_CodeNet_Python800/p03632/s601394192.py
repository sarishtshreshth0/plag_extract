import sys
A, B, C, D = map(int, sys.stdin.readline().split())
s = max(A, C)
f = min(B, D)
if f -s >= 0:
    print(f - s)
else:
    print(0)