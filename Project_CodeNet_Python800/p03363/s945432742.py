import sys
input = sys.stdin.readline
from itertools import accumulate
from collections import Counter


def read():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    return N, A


def solve(N, A):
    S = accumulate(A)
    C = Counter(S)
    ans = 0
    k = 0
    for a in A:
        ans += C[k]
        k += a
        C[k] -= 1
    return ans


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
