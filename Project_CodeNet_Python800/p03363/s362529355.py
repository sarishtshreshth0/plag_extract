import sys
import numpy as np
from collections import Counter
input = sys.stdin.buffer.readline
N = int(input())
A = np.array([0] + list(map(int, input().split())))


def f(n):
    return n * (n - 1) // 2


cumsum = A.cumsum()
ans = 0
for key, value in Counter(cumsum).items():
    ans += f(value)
print(ans)
