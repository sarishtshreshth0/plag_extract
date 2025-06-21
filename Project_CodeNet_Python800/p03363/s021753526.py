import sys
from itertools import accumulate
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    R = [0] + list(accumulate(A))
    D = Counter(R)

    res = 0
    for v in D.values():
        if v >= 2:
            res += v * (v - 1) // 2
    print(res)


if __name__ == '__main__':
    resolve()
