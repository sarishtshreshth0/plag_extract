N = int(input())
W = list(map(int,input().split()))

import numpy as np

w = np.cumsum(W)

print(int(min(abs(sum(W)/2 - w))*2))