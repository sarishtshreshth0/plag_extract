#
#https://www.youtube.com/watch?v=igfVeTsGeYw
#https://atcoder.jp/contests/abc121/tasks/abc121_d
#
import numpy as np
import sys

input = sys.stdin.readline

A,B = map(int,input().split())

def calc(x):
    if (x+1)%4 == 0:
        return 0
    elif (x+1)%4 == 1:
        return x
    elif (x+1)%4 == 2:
        return (x-1)^x
    else:
        return (x-2)^(x-1)^x

if A!=0:A-=1

print(calc(A)^(calc(B)))

