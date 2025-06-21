import sys
a, b, c, d = map(int, input().split())
if b<=c or d<=a:
    print(0)
    sys.exit()
print(min(b,d) - max(a,c))