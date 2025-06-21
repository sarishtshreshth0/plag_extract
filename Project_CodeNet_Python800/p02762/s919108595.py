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
sys.setrecursionlimit(10**9)
mod = 10**9+7

class UnionFind:
  def __init__(self,n):
    self.n=[-1]*n
    self.r=[0]*n
  def find_root(self,x):
    if self.n[x]<0:
      return x
    else:
      self.n[x]=self.find_root(self.n[x])
      return self.n[x]
  def unite(self,x,y):
    x=self.find_root(x)
    y=self.find_root(y)
    if x==y:return
    elif self.r[x]>self.r[y]:
      self.n[x]+=self.n[y]
      self.n[y]=x
    else:
      self.n[y]+=self.n[x]
      self.n[x]=y
      if self.r[x]==self.r[y]:
        self.r[y]+=1
  def root_same(self,x,y):
    return self.find_root(x)==self.find_root(y)
  def count(self,x):
    return -self.n[self.find_root(x)]

N,M,K = map(int,input().split())
u = UnionFind(N)
blocks = [0]*N
f_count = [0]*N
for i in range(M):
    a,b = I()
    f_count[a-1] += 1
    f_count[b-1] += 1
    u.unite(a-1,b-1)
for i in range(K):
    c,d = I()
    if u.root_same(c-1,d-1):
        blocks[c-1] += 1
        blocks[d-1] += 1
for i in range(N):
    print(u.count(i)-f_count[i]-blocks[i]-1)