import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9 + 7

a,b = map(int,input().split())
if a == 1 and b == 1:
    print("Draw")
elif a == 1:
    print("Alice")
elif b == 1:
    print("Bob")
elif a > b:
    print("Alice")
elif a == b:
    print("Draw")
else:
    print("Bob")