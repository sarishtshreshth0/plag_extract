#!/usr/bin/env python3
n, m, *x = map(int, open(0).read().split())
if n >= m:
    print(0)
    quit()
x.sort()
a = []
for i in range(m-1):
    a += [x[i+1]-x[i]]
a.sort()
ans = sum(a[:m-n])
print(ans)
