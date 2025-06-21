import sys
sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def MS(): return input().split()
def LS(): return list(input())
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def printlist(lst, k=' '): print(k.join(list(map(str, lst))))
INF = float('inf')
from math import ceil, floor, log2,sqrt
# from collections import deque, defaultdict
from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    N, D = MI()
    X = []
    for i in range(N):
        X.append(LI())
        
    # print(X)
    ans = 0
    for i, j in product(range(N), repeat=2):
        if i == j:
            continue
        Y = X[i]
        Z = X[j]
        dist = 0
        for d in range(D):
            dist += (Y[d] - Z[d])**2
        sq = sqrt(dist)
        # print(dist, sq, dist % sq)
        if dist % sq == 0:
            ans += 1
    print(ans // 2)

if __name__ == '__main__':
    solve()

