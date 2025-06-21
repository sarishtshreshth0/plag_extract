from math import ceil
from sys import stdin
H, W = [int(_) for _ in stdin.readline().rstrip().split()]
if H == 1 or W == 1:
    print(1)
else:
    print(ceil(H*W/2))