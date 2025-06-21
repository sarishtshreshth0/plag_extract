# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
def run():
    N = int(input())
    S = input()
    position = 0
    l = 0
    r = 0
    for s in S:
        if s == '(':
            position += 1
        else:
            position -= 1
        if position < 0:
            l += abs(position)
            position = 0
    r += position

    print(l * '(' + S + r * ')')

if __name__ == "__main__":
    run()
