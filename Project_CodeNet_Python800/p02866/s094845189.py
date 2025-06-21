# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque

def run():
    N = int(sysread())
    D = list(map(int, sysread().split()))
    mod = 998244353
    dict = defaultdict(lambda:[])
    max_depth = 0
    for node, d in enumerate(D, 1):
        dict[d].append(node)
        max_depth = max(max_depth, d)
    if dict[0] != [1]:
        print(0)
        return None

    ans = 1
    for i in range(1, max_depth+1):
        pre = len(dict[i-1])
        current = len(dict[i])
        val =pow(pre, current, mod)
        ans *= val
        ans %= mod
    print(ans)
    return None

    #print(factorials)
if __name__ == "__main__":
    run()