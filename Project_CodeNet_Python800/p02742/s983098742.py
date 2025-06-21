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
#    P = [list(map(int,input().split())) for _ in range(M)]

H,W=map(int, input().split())

if H==1 or W==1:
    print(1)
    sys.exit()

print(ceil(H/2)*ceil(W/2) + floor(H/2)*floor(W/2))
