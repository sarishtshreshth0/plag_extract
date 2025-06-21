#!/usr/bin/env python3
n = int(input())
c = 10
for i in reversed(range(1, int(-(-(n**0.5) // 1)) + 1)):
    if n % i < 1:
        c = min(c, max(len(str(n // i)), len(str(i))))
print(c)
