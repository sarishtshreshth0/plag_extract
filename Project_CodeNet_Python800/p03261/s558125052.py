#!/usr/bin/env python3
n, *w = open(0).read().split()
s = set(w)
if len(s) != len(w):
    print("No")
    exit()
for i in range(1, int(n)):
    if w[i][0] != w[i - 1][-1]:
        print("No")
        exit()
print("Yes")
