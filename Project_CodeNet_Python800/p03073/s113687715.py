#!/usr/bin/env python3
s = list(input())
a1 = 0
a2 = 0
for i in range(len(s)):
    a1 += int(s[i]) == i % 2
    a2 += int(s[i]) != i % 2
print(min(a1, a2))
