# -*- coding: utf-8 -*-
"""
Created on Sat May  9 23:33:40 2020

@author: shinba
"""

q,h,s,d = map(int,input().split())

n = int(input())

a = [4*q,2*h,s,d/2]

a.sort()

if a[0] != d/2:
    print(int(n*a[0]))

else:
    if n % 2 == 0:
        print(d*int(n/2))
    else:
        print(d*int(n/2)+int(a[1]))
