#!/usr/bin/env python3

Q, H, S, D = [int(x) for x in input().split(" ")]
N = int(input())

if S > Q * 4:
    S = Q * 4
if S > H * 2:
    S = H * 2
if D > S * 2:
    D = S * 2
ans = (N // 2) * D + (N % 2) * S
print(ans)
