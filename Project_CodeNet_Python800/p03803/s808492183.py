#import sys
#import numpy as np
import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
a,b=map(int,input().split())
if a==b:
  print("Draw")
elif a==1:
  print("Alice")
elif b==1:
  print("Bob")
elif a<b:
  print("Bob")
elif a>b:
  print("Alice")
