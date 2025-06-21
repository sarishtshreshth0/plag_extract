#https://atcoder.jp/contests/abc109/tasks/abc109_c
import numpy as np
import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

N,X = map(int,input().split())
City = np.array(list(map(int,input().split())))
City = np.sort(np.append(City,[X]))
kaisa = np.diff(City)
print(gcd_list(kaisa))

