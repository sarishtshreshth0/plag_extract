import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n,m = map(int,ipt().split())
    job = [[] for i in range(m+1)]
    for i in range(n):
        a,b = map(int,ipt().split())
        if a <= m:
            job[a].append(-b)
    ma = 0
    hq = []
    for i in range(m+1):
        for j in job[i]:
            hpq.heappush(hq,j)
        if hq:
            ma += hpq.heappop(hq)
    print(-ma)

    return None

if __name__ == '__main__':
    main()
