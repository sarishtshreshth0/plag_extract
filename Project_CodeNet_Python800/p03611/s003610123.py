from collections import Counter
import numpy as np
n = int(input())
a = np.array([int(i) for i in input().split()])
b = a+1
c = a-1
d = np.concatenate([a,b,c])
e = Counter(d)
print(max(e.values()))