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
w=lmp()
l=[0]*n
l[0]=w[0]
for i in range(1,n):
    l[i]=l[i-1]+w[i]
ans=10**10
for i in range(n):
    ans=min(ans,abs(l[-1]-2*l[i]))
print(ans)