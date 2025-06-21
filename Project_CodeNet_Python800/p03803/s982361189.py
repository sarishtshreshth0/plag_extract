from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A, B = map(int, input().split())

    if A == B:
        print('Draw')
    elif A == 1 or 0 < A - B < 12:
        print('Alice')
    elif B == 1 or A < B:
        print('Bob')

if __name__ == '__main__':
    main()