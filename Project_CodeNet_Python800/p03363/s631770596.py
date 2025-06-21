import sys
import numpy as np
from collections import Counter
input = sys.stdin.buffer.readline
N = int(input())
A = np.array(list(map(int, input().split())))


def f(n):
    return n * (n - 1) // 2


cumsum = A.cumsum()
ans = 0
for key, value in Counter(cumsum).items():
    if key == 0:
        ans += value
    if value >= 2:
        ans += f(value)
print(ans)
