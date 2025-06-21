import sys

h, w = list(map(int, input().split()))

if h == 1 or w == 1:
    print(1)
    sys.exit()

print(int((h * w + 1)/2))
