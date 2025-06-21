import math
import sys
from collections import deque
import heapq
import copy
import itertools
from itertools import permutations
def mi() : return map(int,sys.stdin.readline().split())
def ii() : return int(sys.stdin.readline().rstrip())
def i() : return sys.stdin.readline().rstrip()
a=ii()
l=list(i())
ans=1
for i in range(a-1):
  if l[i]!=l[i+1]:
    ans+=1
print(ans)