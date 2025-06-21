import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)

H, W = map(int, readline().split())

import math

if H == 1 or W == 1:
    print(1)
    exit()

total = H * W
ans = (total + 2 - 1) // 2
print(ans)