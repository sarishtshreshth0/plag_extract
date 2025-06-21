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

n=int(input())
a=lmp()
s=[0]*n
s[0]=a[0]
for i in range(1,n):
    s[i]=s[i-1]+a[i]
s.append(0)
q=Counter(s).values()

ans=0
for i in q:
    ans+=i*(i-1)//2
print(ans)