import numpy as np
N, M = map(int, input().split())
X = list(map(int, input().split()))
X_sort = np.array(sorted(X))

diff_arr = X_sort[1:] - X_sort[:M-1]
print(sum(sorted(diff_arr, reverse = True)[N-1:]))