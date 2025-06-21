import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline()[:-1]
from bisect import *
from collections import *
from heapq import *
from fractions import Fraction

a, c, b = map(int, input().split())
if a <= b <= c or c <= b <= a:
    print('Yes')
else:
    print('No')
