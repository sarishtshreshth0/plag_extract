#!/usr/bin/env python3
import math
import sys

n = int(input())

a = math.ceil(math.sqrt(n))

ans = sys.maxsize

for i in range(1, a + 1):
    if (n % i) == 0:
        ans = min(ans, max(i, n / i))

print(int(math.log10(ans) + 1))
