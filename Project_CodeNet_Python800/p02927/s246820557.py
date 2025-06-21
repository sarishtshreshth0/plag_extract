import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

M, D = map(int, input().split())

ans = 0
for i in range(1, M + 1):
    for j in range(1, D + 1):
        d1 = j // 10
        d2 = j % 10
        if d1 < 2 or d2 < 2:
            continue
        if d1 * d2 == i:
            ans += 1
print(ans)
