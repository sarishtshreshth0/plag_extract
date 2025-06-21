# https://atcoder.jp/contests/abc117/tasks/abc117_c

import numpy as np

N, M = list(map(int, input().split()))
Xs = list(map(int, input().split()))

x = np.array(sorted(Xs))
if N == 1:
    print(np.sum(np.sort(np.diff(x))))
else:
    print(np.sum(np.sort(np.diff(x))[:-N+1]))