#import pysnooper
#import numpy
#import os,re,sys,operator
#from collections import Counter,deque
#from operator import itemgetter,mul
#from itertools import accumulate,combinations,groupby,combinations_with_replacement,permutations
from sys import stdin,setrecursionlimit
#from bisect import bisect_left,bisect_right
#from copy import deepcopy
#import heapq
#import math
#import string
#from time import time
#from functools import lru_cache,reduce
#from math import factorial,hypot
#import sys
#from fractions import gcd
setrecursionlimit(10**6)
input=stdin.readline

m,d=map(int,input().split())
ans=0
for i in range(1,m+1):
    for j in range(1,d+1):
        s=str(j)
        if len(s)>=2:
            o,t=int(s[0]),int(s[1])
            if o>=2 and t>=2 and o*t==i:
                #print(i,j)
                ans+=1
print(ans)