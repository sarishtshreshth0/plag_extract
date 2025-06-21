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
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
def gcd(*numbers): reduce(math.gcd, numbers)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
count = 0
ans = 0

Q,H,S,D = I()
N = i()

a = N // 2
b = N // 1
c = N // 0.5
d = N // 0.25

H = min(H, Q*2)
S = min(S, H*2)
D = min(D, S*2)

if N % 2 == 0:
    print(D*(N//2))
else:
    print(D*(N//2)+S)
