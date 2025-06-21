
#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def int_mtx(N):
    x = []
    for _ in range(N):
        x.append(input())
    return x

def int_map():
    return map(int,input().split())

def int_list():
    return list(map(int,input().split()))

import collections as col

N = int(input())
a = int_list()

c = col.Counter(a)

ans = 0

for i in range(1,100000):
    ans = max(ans,c[i-1]+c[i]+c[i+1])

print(ans)