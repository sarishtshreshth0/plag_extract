import sys
from collections import deque

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

Q, H, S, D = lr()
N = ir()

H = min(Q * 2, H)
S = min(H * 2, S)
if S * 2 <= D:
    print(S * N)
else:
    print((N // 2) * D + (N % 2) * S)
