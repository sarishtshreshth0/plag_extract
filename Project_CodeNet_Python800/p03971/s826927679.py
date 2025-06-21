#!/usr/bin/env python3

# from numba import njit

# from collections import Counter
# from itertools import accumulate
# import numpy as np
# from heapq import heappop,heappush
# from bisect import bisect_left

# @njit
def solve(n,a,b,s):
  ans = [""]*n
  japaneseStudents = 0
  foreignStudents = 0
  for i in range(n):
    if s[i] == "a" and japaneseStudents + foreignStudents < a+b:
      ans[i] = "Yes"
      japaneseStudents += 1
    elif s[i] == "b" and japaneseStudents + foreignStudents < a+b and foreignStudents < b:
      ans[i] = "Yes"
      foreignStudents += 1
    else:
      ans[i] = "No"
  return ans



def main():
  N,A,B = map(int,input().split())
  s = input()
  ans = solve(N,A,B,s)
  for i in range(N):
    print(ans[i])
  return

if __name__ == '__main__':
  main()
