#!/usr/bin/env python3
(*p, ) = map(int, input().split())
n = int(input())

m = min(p[0] * 8, p[1] * 4, p[2] * 2, p[3])
m2 = min(p[0] * 4, p[1] * 2, p[2])

if m == p[3]:
    print(n // 2 * m + n % 2 * m2)
else:
    print(n * m // 2)
