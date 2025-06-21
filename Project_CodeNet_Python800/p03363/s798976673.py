import math
import numpy as np
import queue
from collections import deque,defaultdict
import heapq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n = int(ipt())
    a = [int(i) for i in ipt().split()]
    d = defaultdict(int)
    sa = 0
    for i in a:
        sa += i
        d[sa] += 1
    ans = 0
    for iv in d.values():
        ans += iv*(iv-1)//2
    print(ans+d[0])
    return

if __name__ == '__main__':
    main()
