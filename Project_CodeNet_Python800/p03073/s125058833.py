# -*- coding: utf-8 -*-
 
## Library
 
import sys
from fractions import gcd
import math
from math import ceil,floor
import collections
from collections import Counter
import itertools
 
## input
 
# N=int(input())
# A,B,C,D=map(int, input().split())
# S = input()
# yoko = list(map(int, input().split()))
# tate = [int(input()) for _ in range(N)]
# N, M = map(int,input().split()) 
#    P = [list(map(int,input().split())) for i in range(M)]
 
S = input()

min1 = 0 # 01010101
min2 = 0 # 10101010


for i in range(len(S)):
    if i%2==0:
        if S[i]=="0":
            min2 += 1
        else:
            min1 += 1
    else:
        if S[i]=="1":
            min2 += 1
        else:
            min1 += 1

print(min(min1,min2))