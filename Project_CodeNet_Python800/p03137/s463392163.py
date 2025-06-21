import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7

N, M = I()
X = l()
X.sort()
kyori = []

if N >= M:
    print(0)
    sys.exit()

if M == 1:
    print(0)
    sys.exit()
for i in range(len(X)-1):
    s = X[i+1]-X[i]
    kyori.append(s)

kyori.sort()
kyori.reverse()

for j in range(N-1):
    kyori.pop(0)

print(sum(kyori))
