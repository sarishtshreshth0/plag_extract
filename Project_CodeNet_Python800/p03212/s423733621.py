import random as rng
import itertools as it
import collections as col
import heapq as hq
import sys
import copy as cp
sys.setrecursionlimit(10**9)


def dump_impl(*objects):
    print(*objects, file=sys.stderr)


def dump_dummy(*objects):
    pass


dump = dump_impl if "DEBUG" in sys.argv else dump_dummy

N = int(input())

ans = 0
for n in range(3, 10):
    for l in it.product(["7", "5", "3"], repeat=n):
        if "7" not in l or "5" not in l or "3" not in l:
            continue
        M = int("".join(l))
        if M <= N:
            dump(M, ans)
            ans += 1
dump(N)
print(ans)
