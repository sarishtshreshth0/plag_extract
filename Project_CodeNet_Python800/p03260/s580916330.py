from collections import deque
from collections import Counter
from itertools import product, permutations,combinations
from operator import itemgetter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right, bisect
#pypyではscipy, numpyは使えない
#from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson, minimum_spanning_tree
#from scipy.sparse import csr_matrix, coo_matrix, lil_matrix
#import numpy as np
from fractions import gcd
from math import ceil,floor, sqrt, cos, sin, pi, factorial
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**8)
INF = float('inf')
from datetime import datetime as dt

def main():
  a, b = map(int, readline().split())
  if a*b%2==1:
    print('Yes')
  else:
    print('No')
  
  
  
if __name__ == '__main__':
  main()