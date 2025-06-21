import sys
import numpy as np
import math
import collections
import copy
from collections import deque 
from functools import reduce
from itertools import product
from itertools import combinations

N = int(input())
An = list(map(int, input().split()))
Bn = []
Bn.append(0)
for i, A in enumerate(An):
    Bn.append(A+Bn[i])
Cn = collections.Counter(Bn)
ans = 0
for c in Cn.values():
    if c < 2:
        continue
    ans += c * (c-1) // 2
print(ans)



