# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
from heapq import heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7

def mapline(t = int):
    return map(t, sysread().split())
def mapread(t = int):
    return map(t, read().split())

def counts(A):
    L = A.bit_length()
    ans = 0
    for l in range(L):
        if l == 0:
            s = A // 2
            s = s % 2
            if A % 2:
                ans = s ^ 1
            else:
                ans = s
        else:
            if (A >> l) & 1:
                v = A - ((A >> l) << l) + 1
                if v % 2:
                    ans |= 1 << l
    return ans

def run():
    A, B = mapline()
    a = counts(A-1)
    b = counts(B)

    print(a ^ b)
if __name__ == "__main__":
    run()
