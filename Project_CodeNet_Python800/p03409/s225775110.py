def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    n = int(input())
    red, blue = [-1]*2*n, [-1]*2*n

    for _ in range(n):
        a,b = map(int, input().split())
        red[a] = b
    for _ in range(n):
        a,b = map(int, input().split())
        blue[a] = b

    kouho = []
    res = 0
    for i in range(2*n-1, -1, -1):
        if blue[i] >= 0:
            kouho.append(blue[i])
        else:
            kouho.sort()
            for j in range(len(kouho)):
                if red[i] < kouho[j]:
                    kouho.pop(j)
                    res += 1
                    break
    print(res)

if __name__ == '__main__':
    main()