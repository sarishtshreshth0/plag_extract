# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
from heapq import heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal

INF = 1 << 50

def eval(start, CSF):
    N = len(CSF)+1
    queue = []
    heappush(queue, (0, start))
    while queue:
        time, current = heappop(queue)
        #print(f'time : {time}, current : {current}')
        if current == N-1:break
        for i in range(current, current+1):
            c,s,f = CSF[i]
            first_s = s + c * (current-i)
            if time <= first_s:
                next_leave = first_s
            else:
                next_leave = first_s + math.ceil((time - first_s) / f) * f
            #print(f'i : {i}, c/s/f : {c}/{s}/{f}, next_leave : {next_leave}')
            heappush(queue, (next_leave + c, current+1))
    return time

def run():
    N = int(sysread())
    CSF = []
    for i in range(N-1):
        c,s,f = map(int, sysread().split())
        CSF.append((c,s,f))

    for i in range(N-1):
        print(eval(i, CSF))
    print(0)
    

if __name__ == "__main__":
    run()