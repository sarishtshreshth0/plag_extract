import sys
input = sys.stdin.readline
import math
from functools import reduce


def read():
    N = int(input().strip())
    W = []
    for i in range(N):
        w = input().strip()
        W.append(w)
    return N, W


def solve(N, W):
    used = dict()
    for w in W:
        if w in used.keys():
            return "No"
        used[w] = True
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            return "No"
    return "Yes"


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
