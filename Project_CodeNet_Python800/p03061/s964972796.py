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

def SMI(): return input().split()
def SLI(): return list(input())

def printlist(lst, k=' '): print(k.join(list(map(str, lst))))
INF = float('inf')

# from math import ceil, floor, log2
# from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np
# from numpy import cumsum  # accumulate

from fractions import gcd

def solve():
    N = II()
    A = LI()

    # 左から累積和的gcd
    L = [1] * N
    L[0] = A[0]
    for i in range(1, N):
        L[i] = gcd(A[i], L[i-1])

    # 右から累積和的gcd
    R = [1] * N
    R[-1] = A[-1]
    for i in range(N-2, -1, -1):
        R[i] = gcd(A[i], R[i+1])

    # print(L)
    # print(R)
    ans = 1
    for i, a in enumerate(A):
        l = i - 1
        r = i + 1
        if l < 0:
            ans = max(ans, R[r])
        elif r >= N:
            ans = max(ans, L[l])
        else:
            ans = max(ans, gcd(L[l], R[r]))
    print(ans)

if __name__ == '__main__':
    solve()
