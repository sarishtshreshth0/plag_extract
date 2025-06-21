import numpy as np
import math
from functools import reduce
N,X,*x = map(int,open(0).read().split())
print(reduce(math.gcd,abs(X - np.array(sorted(x)))))