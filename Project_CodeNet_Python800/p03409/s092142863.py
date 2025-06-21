import math, sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import lru_cache
from heapq import heapify, heappop, heappush
from itertools import accumulate, combinations, permutations
input = sys.stdin.readline
mod = 10**9 + 7
ns = lambda: input().strip()
ni = lambda: int(input().strip())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

def main():
    n = ni()
    red = []
    for _ in range(n):
        red.append(nl())
    blue = []
    for _ in range(n):
        blue.append(nl())

    red.sort(key=lambda x:x[1], reverse=True)
    blue.sort(key=lambda x:x[0], reverse=True)

    #print(red, blue)
    ans = 0
    for _ in range(n):
        mn = blue.pop()
        for i in range(len(red)):
            if mn[0] > red[i][0] and mn[1] > red[i][1]:
                #print(mn, red.pop(i), 'pair')
                red.pop(i)
                ans += 1
                break

    print(ans)
        

if __name__ == '__main__':
    main()