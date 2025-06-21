import numpy as np
import scipy.sparse as sps
import scipy.misc as spm
import collections as col
import functools as func
import itertools as ite
import fractions as frac
import math as ma
from math import cos,sin,tan,sqrt
import cmath as cma
import copy as cp
import sys
import re
import bisect as bs
sys.setrecursionlimit(10**7)
EPS = sys.float_info.epsilon
PI = np.pi; EXP = np.e; INF = np.inf
MOD = 10**9 + 7

def sinput(): return sys.stdin.readline().strip()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(n=0):
    if n: return [0 for _ in range(n)]
    else: return list(imap())
def farr(): return list(fmap())
def sarr(n=0):
    if n: return ["" for _ in range(n)]
    else: return sinput().split()
def adj(n): return [[] for _ in range(n)]

#整数問題セット
def gcd(numbers): return func.reduce(frac.gcd, numbers)
def lcm(numbers): return func.reduce(LCM, numbers)
def inv(a): return pow(a, MOD-2, MOD) #逆元
def comb(n,r):
    ans = 1
    for i in range(r): ans *= n-i; ans *= inv(r-i); ans %= MOD
    return ans

n,a,b = imap()
div,mod = divmod(n,10000)
allEvents = (2**10000%MOD)**div%MOD * 2**mod%MOD
ans = allEvents - comb(n,a) - comb(n,b) - 1
ans %= MOD
print(ans)
