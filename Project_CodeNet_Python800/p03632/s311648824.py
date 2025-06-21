import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

a,b,c,d = map(int,input().split())
print(max(min(b,d)-max(a,c),0))