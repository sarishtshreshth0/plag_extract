from heapq import heapify, heappop, heappush
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import statistics # Pythonのみ
# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    N, M = map(int, input().split())
    jobs=[[] for _ in range(M)]
    for i in range(N):
        a, b = map(int, input().split())
        if a > M:
            continue
        jobs[M-a].append(b)
    
    ans=0
    q=[]
    #q=heapify([])
    for i in reversed(range(M)):
        for b in jobs[i]:
            heappush(q,-b)
        if not q: continue
        ans+= -heappop(q)
    print(ans)
    
    
    

resolve()