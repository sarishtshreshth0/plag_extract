#import sys
#import numpy as np
#import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect

n=int(input())
r=[list(map(int,input().split())) for _ in range(n-1)]
for i in range(n-1):
    time=r[i][1]
    for j in range(i,n-1):
        if time>=r[j][1]:
            if time%r[j][2]==0:
                time+=r[j][0]
            else:
                time=((time//r[j][2])+1)*r[j][2]
                time+=r[j][0]
        else:
            time=r[j][1]
            time+=r[j][0]
    print(time)
print(0)