# -*- coding: utf-8 -*-
 
import math
import itertools
import sys
import copy
 
# 入力
#A, B, C, D = map(int, input().split())
#L = list(map(int, input().split()))
#S = list(str(input()))
#N = int(input())
#S = str(input())
A, B, C = map(int, input().split())

if A > B :
  A, B = B, A
  
if A < C < B :
  print ("Yes")
else :
  print ("No")


