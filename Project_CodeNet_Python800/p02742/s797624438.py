#!/usr/bin/env python3
h, w = map(int, input().split())

cnt = 0

if h == 1 or w == 1:
    print(1)
    exit()

cnt = (w * 2 // 2) * (h // 2)
if h % 2 == 1:
    if w % 2 == 1:
        cnt += w // 2 + 1
    else:
        cnt += w // 2

print(cnt)
