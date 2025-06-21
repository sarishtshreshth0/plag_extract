import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations,combinations, accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush,heapify
from math import ceil, floor, sqrt
from copy import deepcopy
from fractions import gcd

def main():
    num = int(input())
    ans = 2 * num / gcd(2,num)
    print(int(ans))

if __name__ == "__main__":
    main()