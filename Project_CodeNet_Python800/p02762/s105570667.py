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

class unionfind():
    def __init__(self, n):
        self.n = n
        # 中身が負の数なら根であり、数字の絶対値はグループ数
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0: return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
        x,y = self.find(x), self.find(y)
        if x == y: return
        if self.parents[x] > self.parents[y]: x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def size(self, x): return -self.parents[self.find(x)]
    def same(self, x, y): return self.find(x) == self.find(y)
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self): return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self): return len(self.roots())

n,m,k = imap()
uf = unionfind(n)
f,ng,anss = iarr(n),iarr(n),iarr(n)

for i in range(m):
    a,b = imap()
    a,b = a-1,b-1
    f[a] += 1
    f[b] += 1
    uf.union(a,b)

for i in range(n):
    anss[i] = uf.size(i) - f[i] - 1

for i in range(k):
    c,d = imap()
    c,d = c-1,d-1
    if uf.same(c,d):
        anss[c] -= 1
        anss[d] -= 1

print(*anss)
