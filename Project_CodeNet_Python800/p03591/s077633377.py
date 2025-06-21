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

    s = input().rstrip()
    if len(s)<4:
        print('No')
    else:
        if 'YAKI'==s[:4]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()