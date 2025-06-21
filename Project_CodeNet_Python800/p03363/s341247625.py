from collections import Counter
import numpy as np


def solve(n):
    return n * (n - 1) // 2


n = int(input())
arr = np.array(list(map(int, input().split())))

c = list(arr.cumsum())
zero = c.count(0)

c = list((Counter(c)).values())


print(sum([solve(x) for x in c]) + zero)