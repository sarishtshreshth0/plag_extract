import math
h, w = map(int, input().split())
print(math.ceil((h * w) / 2) if h != 1 and w != 1 else 1)