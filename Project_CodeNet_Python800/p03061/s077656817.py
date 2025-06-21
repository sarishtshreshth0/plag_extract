'''
研究室PCでの解答
'''
from math import gcd
#import numpy as np
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7 #998244353
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

def Enumeration(x):
    low = []
    high = []
    for i in range(1,x):
        if i**2 >= x:
            if i**2 == x:
                low.append(i)
            break
        if x%i == 0:
            low.append(i)
            high.append(x//i)
    return high+low[::-1]

def main():
    n = int(ipt())
    p = set()
    a = [int(i) for i in ipt().split()]
    if n == 2:
        print(max(a))
        exit()
    ma = 1
    G = gcd(gcd(a[0],a[1]),a[2])
    p.add(gcd(a[0],a[1]))
    p.add(gcd(a[0],a[2]))
    p.add(gcd(a[2],a[1]))

    for i in Enumeration(G):
        nm = 0
        for ai in a[3::]:
            if ai%i != 0:
                nm += 1
                if nm == 2:
                    break
        if nm < 2:
            if ma < i:
                ma = i
            break

    for i in p:
        for j in Enumeration(i):
            f = True
            for ai in a[3::]:
                if ai%j != 0:
                    f = False
                    break
            if f:
                if ma < j:
                    ma = j
                break

    print(ma)




    return None

if __name__ == '__main__':
    main()
