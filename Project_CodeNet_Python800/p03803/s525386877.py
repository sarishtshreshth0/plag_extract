import sys
from collections import defaultdict, deque
import math

# import copy
from bisect import bisect_left, bisect_right
# import heapq

# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)

def solve():
    a, b = getList()
    if a == b:
        print("Draw")
        return
    if a == 1:
        print("Alice")
        return
    if b == 1:
        print("Bob")
        return
    if a > b:
        print("Alice")
    else:
        print("Bob")

def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()