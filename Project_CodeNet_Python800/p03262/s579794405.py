#!/usr/bin/env python3
from math import gcd
# from numba import njit
from functools import reduce
# from collections import Counter
# from itertools import accumulate
# import numpy as np
# from heapq import heappop,heappush
# from bisect import bisect_left

# @njit
def solve(n,x,a):
    delta_a = (abs(a[i] - x) for i in range(n))
    return reduce(gcd,delta_a)



def main():
    # N = int(input())
    N,X = map(int,input().split())
    a = list(map(int,input().split()))
    print(solve(N,X,a))
    return

if __name__ == '__main__':
    main()
