import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations,combinations, accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush,heapify
from math import ceil, floor, sqrt, gcd
from copy import deepcopy
from functools import reduce


def gcd_list(numbers):
    return reduce(gcd, numbers)

def main():
    n,x = map(int, input().split())
    x_list = list(map(int, input().split()))

    
    list_s = []
    for i in range(n):
        list_s.append(abs(x_list[i]-x))
        
    ans = gcd_list(list_s)
    print(ans)


if __name__ == "__main__":
    main()
