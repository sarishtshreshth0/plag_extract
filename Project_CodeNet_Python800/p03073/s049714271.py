#!/usr/bin/env python3
s = input()
n = len(s)
z = "01" * n
print(
    min(sum(s[i] != z[i] for i in range(n)),
        sum(s[i] != z[i + 1] for i in range(n))))
