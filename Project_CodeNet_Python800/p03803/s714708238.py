import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

a,b=mp()
if a==1 and b==1:
    print("Draw")
    exit()
if a==1:
    print("Alice")
    exit()
if b==1:
    print("Bob")
    exit()
if a==b:
    print("Draw")
    exit()
if a>b:
    print("Alice")
    exit()
if b>a:
    print("Bob")
    exit()
