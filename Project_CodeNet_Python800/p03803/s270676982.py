# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:01:05 2020

@author: shinba
"""

a,b = map(int,input().split())

if a == 1:
    if b == 1:
        print("Draw")
    else:
        print("Alice")
elif b == 1:
    print("Bob")
else:
    if a > b:
        print("Alice")
    elif b > a:
        print("Bob")
    else:
        print("Draw")
