#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
red = [list(map(int,input().split())) for i in range(N)]
blue = [list(map(int,input().split())) for i in range(N)]
red.sort()
blue.sort()

ans = 0
for c,d in blue:
    x = []
    for a,b in red:
        if a < c and b < d:
            x.append([a,b])
    if len(x) > 0:
        ans += 1
        x = sorted(x, key=lambda x:x[1])
        red.remove(x[-1])

print(ans)
