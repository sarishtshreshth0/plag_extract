from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
ans = 0
for x in product([0, 3, 5, 7], repeat=9):
    y = 0
    for i in range(9):
        y += x[8-i] * 10**i
    if y > n:
        break
    if str(y).count('0') == 0 and x.count(3) > 0 and x.count(5) > 0 and x.count(7) > 0:
        ans += 1
print(ans)