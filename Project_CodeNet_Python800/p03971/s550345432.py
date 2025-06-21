# -*- coding: utf-8 -*-

## Library

import sys
from fractions import gcd
import math
from math import ceil,floor
import collections
from collections import Counter

## input

# n=int(input())
# A,B,C,D=map(int, input().split())
# string = input()
# yoko = list(map(int, input().split()))
# tate = [int(input()) for _ in range(N)]
# N, M = map(int,input().split()) 
#    P = [list(map(int,input().split())) for i in range(M)]

N,A,B=map(int, input().split())
S = input()
tmp1 = 0
tmp2 = 0

for i in range(0,N):
    if tmp1 < A+B:
        if S[i] == "a":
            tmp1 += 1
            print("Yes")
        elif (S[i] == "b") & (tmp2 < B):
            tmp1 += 1
            tmp2 += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")
