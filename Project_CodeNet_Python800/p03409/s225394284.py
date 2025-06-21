#!/usr/bin/env python3
(n, ), *dot = [[*map(int, i.split())] for i in open(0)]
red = sorted(dot[:n])
blue = sorted(dot[n:])
for c, d in blue:
    o = [[a, b] for a, b in red if a < c and b < d]
    if o:
        red.remove(max(o, key=lambda x: x[1]))
print(n - len(red))
