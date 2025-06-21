import numpy as np
import math
from functools import reduce

N,X,*x = map(int,open(0).read().split())
x.sort()
nx = np.array(x)
dif_nx = abs(X - nx)
print(reduce(math.gcd,dif_nx))