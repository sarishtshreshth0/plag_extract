# -*- coding: utf-8 -*-
 
## Library
 
import sys
from fractions import gcd
import math
from math import ceil,floor
import collections
from collections import Counter
import itertools
import copy
 
## input
 
# N=int(input())
# A,B,C,D=map(int, input().split())
# S = input()
# yoko = list(map(int, input().split()))
# tate = [int(input()) for _ in range(N)]
# N, M = map(int,input().split()) 
#    P = [list(map(int,input().split())) for i in range(M)]
#    S = []
#    for _ in range(N):
#        S.append(list(input()))
 
N,M = map(int, input().split())
X = list(map(int, input().split()))


X.sort()

ans = X[M-1] - X[0]
tmp = []

if N==1:
    print(ans)
    sys.exit()


for i in range(1,M):
    tmp2 = X[i] - X[i-1]
    if len(tmp) < N-1:
        tmp.append(tmp2)
    else:
        tmp3 = min(tmp)
        if tmp3 < tmp2:
            tmp.remove(tmp3)
            tmp.append(tmp2)

print(ans - sum(tmp))