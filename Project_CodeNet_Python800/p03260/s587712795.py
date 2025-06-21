import itertools
import math
import sys
import heapq
from collections import Counter
from collections import deque
from fractions import gcd
from functools import reduce
INF = 1 << 60
sys.setrecursionlimit(10 ** 6)

#ここから書き始める
a, b = map(int, input().split())
if a % 2 == 1 and b % 2 == 1:
    print("Yes")
else:
    print("No")