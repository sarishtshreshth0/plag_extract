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
from math import ceil, floor, log2
# from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    N = II()
    D = LI()
    mod = 998244353

    C = [0] * (N+1)
    for d in D:
        C[d] += 1
    # print(C)

    # 木が存在するかを判定
    ans = 1
    p = C[0]
    if not(D[0] == 0 and p == 1):
        print(0)
        return
    for i in range(1, N):
        ci = C[i]
        p = ci
        ans = ans * pow(C[i], C[i+1], mod)
    print(ans % mod)


    

if __name__ == '__main__':
    solve()
