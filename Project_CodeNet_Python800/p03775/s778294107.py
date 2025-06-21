# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
#from itertools import product, accumulate, combinations, product
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque

class factorials:
    '''
    args:
      n : max val when exploring factorials
    '''
    def __init__(self, n):
        self.n = 1
        self.factorials = []
        self.update(n)

    def update(self, n):
        if self.n >= n:
            return None
        for i in range(self.n+1, n+1):
            done = False
            limit = int(i ** 0.5)
            for j in self.factorials:
                if j > limit: break
                if not i % j:
                    done = True
                    break
            if not done:
                self.factorials.append(i)
        self.n = n
        return None

    def lists(self):
        return self.factorials

    def check_fact(self, x):
        if x > self.n**2:
            self.update(int(x ** 0.5)+1)
        for f in self.factorials:
            if not x % f:
                return False
        return True

def prod(lis):
    ret = []
    def f(l, product):
        #print(l)
        if not l:
            ret.append(product)
            return None
        for k in l[0]:
            f(l[1:], product + [k])

    f(lis, [])
    return ret

def run():
    N = int(input())
    ori = N
    FACT = factorials(int(N ** 0.5))
    dissociated = defaultdict(lambda:0)
    for f in FACT.lists():
        while not N % f:
            dissociated[f] += 1
            N = N // f
    if N != 1:
        dissociated[N] += 1

    val_dic = {}
    lis = []
    facts = []
    for key in dissociated.keys():
        facts.append(key)
        lis.append(list(range(dissociated[key]+1)))

    products = prod(lis)
    ans = 1 << 50
    for p in products:
        S = 1
        for i, v in enumerate(p):
            S *= facts[i] ** v
        S = max(ori // S, S)
        ans = min(ans, S)

    print(math.floor(math.log10(ans))+1)
    #print(facts, products)
    #print(dissociated)
    #print(lis)


    #print(factorials)
if __name__ == "__main__":
    run()