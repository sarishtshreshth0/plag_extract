input()
from collections import *
from itertools import *
print(sum(v * (v - 1) // 2 for v in Counter([0] + list(accumulate(map(int, input().split())))).values()))