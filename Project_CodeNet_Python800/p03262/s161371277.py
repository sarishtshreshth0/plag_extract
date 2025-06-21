n,x = map(int,input().split())
xl = list(map(int,input().split()))

xl_abs = [abs(x-xl[i]) for i in range(n)]

import math
import functools
print(functools.reduce(math.gcd,xl_abs))