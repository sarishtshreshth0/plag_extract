import sys
A, B, C, D = map(int, input().split())
s, g = 0, 0
if A <= C:
    s = C
    if B < s:
        print(0)
        sys.exit()
else:
    s = A
    if D < s:
        print(0)
        sys.exit()

if B <= D:
    g = B
else:
    g = D

print(g - s)