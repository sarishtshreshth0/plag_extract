def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    m,d = map(int, input().split())
    res = 0
    for i in range(1, m+1):
        for j in range(1, d+1):
            a = j // 10
            b = j % 10
            if a>=2 and b>=2:
                if a*b == i:
                    res += 1
    print(res)


if __name__ == '__main__':
    main()