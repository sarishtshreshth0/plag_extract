N,X = map(int,input().split())
x = list( map(int,input().split()) )

y = sorted(x+[X])
d_y = [y[i]-y[i-1] for i in range(1,N+1)]
import math
from functools import reduce
print( reduce(math.gcd,d_y) )