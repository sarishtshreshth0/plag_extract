
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
from fractions  import gcd
#input=sys.stdin.readline
import bisect
a,b,c,d=map(int,input().split())
if b<=c or d<=a:
    print(0)
else:
    m=max(a,c)
    M=min(b,d)
    print(M-m)
