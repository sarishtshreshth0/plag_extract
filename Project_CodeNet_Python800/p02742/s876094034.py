import math
h, w = map(int, input().split())

out = 0
if min(h, w) == 1:
    out = 1
else:
    out += (h // 2) * 2 * (w // 2) * 2 / 2 + (h % 2) * math.ceil(w / 2) + (w % 2) * math.ceil(h / 2) - (h % 2) * (w % 2)
print(int(out))
