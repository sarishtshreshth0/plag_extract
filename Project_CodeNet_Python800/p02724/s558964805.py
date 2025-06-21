import sys
from sys import exit
from math import gcd, factorial, ceil, floor, sqrt
from bisect import bisect_left, bisect_right
from copy import deepcopy
from heapq import heapify, heappop, heappush
from itertools import permutations, combinations, product, accumulate
from collections import defaultdict, deque
sys.setrecursionlimit(10**7)

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

X = ii()
a = X//500 * 1000
b = (X-X//500*500)//5 * 5
print(a+b)