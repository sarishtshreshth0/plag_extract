# -*- coding: utf-8 -*-

a, b, c, d = map(int, input().split())

start = max(a, c)
end = min(b, d)

result = end - start
if result < 0:
    result = 0

print(result)