'''
自宅用PCでの解答
'''
import math
#import numpy as np
import itertools
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"


def main():
    n,m,k = map(int,ipt().split())
    fl = [[] for i in range(n)]
    bl = [set() for i in range(n)]
    for i in range(m):
        a,b = map(int,ipt().split())
        fl[a-1].append(b-1)
        fl[b-1].append(a-1)
    for i in range(k):
        c,d = map(int,ipt().split())
        bl[c-1].add(d-1)
        bl[d-1].add(c-1)

    ans = [-1]*n
    al = [True]*n
    for i in range(n):
        if al[i]:
            q = [i]
            al[i] = False
            st = set([i])
            while q:
                qi = q.pop()
                for j in fl[qi]:
                    if al[j]:
                        st.add(j)
                        al[j] = False
                        q.append(j)
            lst = len(st)
            for j in st:
                tmp = lst-len(fl[j])-1
                for k in bl[j]:
                    if k in st:
                        tmp -= 1
                ans[j] = tmp

    print(" ".join(map(str,ans)))


    return None

if __name__ == '__main__':
    main()
