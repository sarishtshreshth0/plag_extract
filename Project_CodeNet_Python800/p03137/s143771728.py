import numpy as np
N, M = map(int, input().split())
X = list(map(int, input().split()))
sortX = np.array(sorted(X), dtype=np.int64)
diffX = np.sort(np.diff(sortX))
if N == 1:
    print(np.sum(diffX))
    exit()
ans = np.sum(diffX[:-(N-1)])
print(ans)
