#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
n=int(input())
s=input()
ans=n
for i in range(1,n):
    if s[i]==s[i-1]:
        ans-=1
print(ans)