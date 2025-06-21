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

Mod=998244353

n=int(input())
d=list(map(int,input().split()))
c=Counter(d)
ans=1
if d[0]!=0:
  print(0)
  exit()
for i in c:
  if i==0:
    if c[i]!=1:
      print(0)
      exit()
  else:
    if i-1 not in c:
      print(0)
      exit()
    else:
      ans*=pow(c[i-1],c[i],Mod)
      ans%=Mod
print(ans)