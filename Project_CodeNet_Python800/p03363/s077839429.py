from collections import Counter, deque  # https://note.nkmk.me/python-scipy-connected-components/
# from copy import copy, deepcopy
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import string
import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    from itertools import accumulate

    B = [0] + A
    # 累積和を格納したリスト．A[l:r]の総和はB[r] - B[l]
    B = list(accumulate(B))
    BB = Counter(B)

    cnt = 0
    for k, v in BB.items():
        if v >= 2:
            cnt += (v*(v - 1) // 2)
    print(cnt)


resolve()