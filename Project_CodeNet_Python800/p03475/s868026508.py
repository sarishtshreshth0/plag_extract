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
# from math import ceil, floor, log2
# from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    N = II()
    L = []
    for i in range(N-1):
        c, s, f = MI()
        L.append([i, s])
        for j in range(i+1):
            k, t = L[j-1]
            if s <= t:
                if t % f == 0:
                    L[j-1] = [k, t+c]
                else:
                    t = t + f - (t % f)
                    L[j-1] = [k, t+c]
            else:
                L[j-1] = [k, s+c]
    # print(L)

    for (i, t) in L:
        print(t)
    print(0)
            
        
        
if __name__ == '__main__':
    solve()
