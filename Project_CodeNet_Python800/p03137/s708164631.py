#!/usr/bin/env python3
n, m = map(int, input().split())
*x, = map(int, input().split())
x.sort()
d = sorted(x[i] - x[i - 1] for i in range(1, m))
print(sum(d[:m - n]) if m > n else 0)
