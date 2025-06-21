import numpy as np
n,m = map(int, input().split())
X = sorted(np.array(input().split(), dtype = np.int64))
X = sorted(np.diff(X))
if m-n >= 0:
    ans = sum(X[:m-n])
else:
    ans = 0
print(ans)