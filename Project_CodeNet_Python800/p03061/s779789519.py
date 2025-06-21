import sys
import os
import math
import bisect
import itertools
import collections
import heapq
import queue
import array

# 時々使う
# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
# from decimal import Decimal
# from collections import defaultdict, deque

# 再帰の制限設定
sys.setrecursionlimit(10000000)


def ii(): return int(sys.stdin.buffer.readline().rstrip())
def il(): return list(map(int, sys.stdin.buffer.readline().split()))
def fl(): return list(map(float, sys.stdin.buffer.readline().split()))
def iln(n): return [int(sys.stdin.buffer.readline().rstrip())
                    for _ in range(n)]


def iss(): return sys.stdin.buffer.readline().decode().rstrip()
def sl(): return list(map(str, sys.stdin.buffer.readline().decode().split()))
def isn(n): return [sys.stdin.buffer.readline().decode().rstrip()
                    for _ in range(n)]


def lcm(x, y): return (x * y) // math.gcd(x, y)


# MOD = 10 ** 9 + 7
MOD = 998244353
INF = float('inf')


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    A = il()
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    # 予めGCDを計算する
    for i in range(N):
        # 左から累積したGCD
        left[i+1] = math.gcd(left[i], A[i])
    for i in reversed(range(N)):
        # 右から累積したGCD
        right[i] = math.gcd(right[i+1], A[i])

    ret = 0
    for i in range(N):
        ret = max(ret, math.gcd(left[i], right[i+1]))
    print(ret)

    
if __name__ == '__main__':
    main()
