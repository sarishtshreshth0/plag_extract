#!/usr/bin/env python3
a, b, c, d = map(int, input().split())
arr = [0] * 101

for i in range(a, b + 1):
    arr[i] += 1

for j in range(c, d + 1):
    arr[j] += 1

ans = len([cnt for cnt in arr if cnt >= 2])

print(ans - 1 if ans != 0 else 0)

