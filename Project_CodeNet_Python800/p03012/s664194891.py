#!/usr/bin/env python3
n, *w = map(int, open(0).read().split())
s = sum(w)
print(min(abs(s - 2 * sum(w[:i + 1])) for i in range(n)))
