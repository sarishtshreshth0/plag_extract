import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)

H, W = map(int, readline().split())

import math

if W == 1 or H == 1:
    print(1)
    exit()

w_can = W // 2
ans = w_can * H
if W % 2 != 0:
    ans += math.ceil(H / 2)

print(ans)