#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

a,b,c=map(int,input().split())
if a<=c<=b or a>=c>=b:
    print("Yes")
else:
    print("No")