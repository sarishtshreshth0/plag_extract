# -*- coding: utf-8 -*-

n = int(input())

s = input()

ans = 1
tmp = s[0]

for c in s:
    if tmp != c:
        ans += 1
        tmp = c

print(ans)
