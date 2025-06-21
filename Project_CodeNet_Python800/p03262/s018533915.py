import sys
input = sys.stdin.readline
import math
from functools import reduce


def read():
    N, X = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    return N, X, A


def solve(N, X, A):
    A = [a-X for a in A]
    ans = reduce(math.gcd, A)
    return abs(ans)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
