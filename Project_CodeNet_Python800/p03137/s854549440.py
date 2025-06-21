#!/usr/bin/env python3

# from numba import njit

import itertools
from bisect import bisect_right,bisect_left

INF = 10**10

# @njit
def solve(n,m,x):
  if n >= m:
    return 0
  else:
    d = list(sorted(x[i+1] - x[i] for i in range(m-1)))[::-1]
    res = x[-1] - x[0]
    for i in range(min(m-1,n-1)):
        res -= d[i]
    return res

def main():
  N,M = map(int,input().split())
  x = sorted(list(map(int,input().split())))
  print(solve(N,M,x))
  return

if __name__ == '__main__':
  main()
