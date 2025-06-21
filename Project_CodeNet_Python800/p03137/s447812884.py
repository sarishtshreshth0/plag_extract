import numpy as np
import sys
n, m = map(int, input().split())
if n >= m:
    print(0)
    sys.exit()
x = [int(i) for i in input().split()]
x = np.array(sorted(x))
diff = np.abs(np.diff(x))
diff = sorted(diff)
if n == 1:
    print(sum(diff))
else:
    print(sum(diff[:-n + 1]))