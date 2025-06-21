import sys
import numpy as np
from collections import Counter
import math

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    A = np.array(readline().split(), np.int64)
    A_cum = np.cumsum(A)
    counter = Counter(A_cum)

    def cmb(n, r):
        return math.factorial(n) // (math.factorial(r)*math.factorial(n-r))

    ans = 0
    for key, value in counter.items():
        if value >= 2:
            ans += cmb(value, 2)
        if key == 0:
            ans += value
    print(ans)


if __name__ == '__main__':
    main()
