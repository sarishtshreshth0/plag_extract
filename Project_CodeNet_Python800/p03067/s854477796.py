#!/usr/bin/env python3
a,b,c = map(int,input().split())

if a > b: a,b = b,a
if a < c and c < b: print("Yes")
else: print("No")