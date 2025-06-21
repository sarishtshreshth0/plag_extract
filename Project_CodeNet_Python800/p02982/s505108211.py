import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n,d=mp()
l=[]
for i in range(n):
    l.append(lmp())
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        a=0
        for k in range(d):
            a+=(l[i][k]-l[j][k])**2
        if (a ** .5).is_integer():
            ans+=1
print(ans)