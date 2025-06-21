#!/usr/bin/env python3

# from numba import njit

# from collections import Counter
# from itertools import accumulate
# import numpy as np
# from heapq import heappop,heappush
# from bisect import bisect_left

# @njit
def solve(n,m):
  if n == 1 or m == 1:
    return 1
  else:
    return (n*m + 1)// 2



def main():
  N,M = map(int,input().split())
  # a = list(map(int,input().split()))
  print(solve(N,M))
  return

if __name__ == '__main__':
  main()
