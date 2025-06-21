#!/usr/bin/env python3

H,W = [int(x) for x in input().split(" ")]

if H == 1 or W == 1:
    ans = 1
elif H % 2 == 0 or W % 2 == 0:
    ans = (H * W) // 2
else:
    ans = (H - 1) * W // 2 + (W + 1) //2

print(ans)
