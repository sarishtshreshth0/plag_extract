import numpy as np
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect


A, B = list(map(int, input().split()))


# def f(x):
#     if x % 4 == 3:
#         return 0
#     elif x % 4 == 0:
#         return x
#     elif x % 4 == 1:
#         return x ^ (x-1)
#     elif x % 4 == 2:
#         return x ^ (x-1) ^ (x-2)


def f(n):
    if (n % 4 == 0):
        return n
    elif (n % 4 == 1):
        return (n ^ (n-1))
    elif (n % 4 == 2):
        return (n ^ (n-1) ^ (n-2))
    else:
        return 0


print(f(A-1) ^ f(B))
