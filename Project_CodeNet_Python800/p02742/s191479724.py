import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

from math import ceil
H, W = mapint()
if H==1 or W==1:
    print(1)
else:
    print(ceil(H*W/2))