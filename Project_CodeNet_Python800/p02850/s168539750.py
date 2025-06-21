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
    n = int(ipt())
    way = [[] for i in range(n+1)]
    for i in range(n-1):
        a,b = map(int,ipt().split())
        way[a].append((b,i))
        way[b].append((a,i))

    q = queue.Queue()
    q.put((1,-1,-1)) #nowplace,pastplace,hen
    col = [-1]*(n-1)
    while not q.empty():
        np,pp,hen = q.get()
        nc = 1
        for i,wn in way[np]:
            if i == pp:
                continue
            if nc == hen:
                nc += 1
            col[wn] = nc
            q.put((i,np,nc))
            nc += 1
    print(max(col))
    for i in col:
        print(i)

    return

if __name__ == '__main__':
    main()
