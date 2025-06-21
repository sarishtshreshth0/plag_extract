import sys
from sys import exit
from collections import deque
from copy import deepcopy
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import heapify, heappop, heappush
from itertools import product, permutations, combinations, combinations_with_replacement
from functools import reduce
from math import gcd, sin, cos, tan, asin, acos, atan, degrees, radians

sys.setrecursionlimit(10**6)
INF = 10**20
eps = 1.0e-20
MOD = 10**9+7

def lcm(x,y):
    return x*y//gcd(x,y)
def lgcd(l):
    return reduce(gcd,l)
def llcm(l):
    return reduce(lcm,l)
def powmod(n,i,mod=MOD):
    return pow(n,mod-1+i,mod) if i<0 else pow(n,i,mod)
def div2(x):
    return x.bit_length()
def div10(x):
    return len(str(x))-(x==0)
def intput():
    return int(input())
def mint():
    return map(int,input().split())
def lint():
    return list(map(int,input().split()))
def ilint():
    return int(input()), list(map(int,input().split()))
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)
def ston(c, c0='a'):
    return ord(c)-ord(c0)
def ntos(x, c0='a'):
    return chr(x+ord(c0))
class counter(dict):
    def __init__(self, *args):
        super().__init__(args)
    def add(self,x,d=1):
        self.setdefault(x,0)
        self[x] += d
    def list(self):
        l = []
        for k in self:
            l.extend([k]*self[k])
        return l
class comb():
    def __init__(self, n, mod=None):
        self.l = [1]
        self.n = n
        self.mod = mod
    def get(self,k):
        l,n,mod = self.l, self.n, self.mod
        k = n-k if k>n//2 else k
        while len(l)<=k:
            i = len(l)
            l.append(l[i-1]*(n+1-i)//i if mod==None else (l[i-1]*(n+1-i)*powmod(i,-1,mod))%mod)
        return l[k]
def pf(x,mode='counter'):
    C = counter()
    p = 2
    while x>1:
        k = 0
        while x%p==0:
            x //= p
            k += 1
        if k>0:
            C.add(p,k)
        p = p+2-(p==2) if p*p<x else x
    if mode=='counter':
        return C
    S = set([1])
    for k in C:
        T = deepcopy(S)
        for x in T:
            for i in range(1,C[k]+1):
                S.add(x*(k**i))
    if mode=='set':
        return S
    if mode=='list':
        return sorted(list(S))

class UnionFind():
    
    # インデックスは0-start
    # 初期化
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n
        self.group = n
    
    # private function
    def root(self, x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]
    
    # x,yが属するグループの結合
    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x==y:
            return
        
        if self.parents[x]>self.parents[y]:
            x,y = y,x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.group -= 1
    
    # x,yが同グループか判定
    def same(self, x, y):
        return self.root(x)==self.root(y)

    # xと同じグループの要素数を取得
    def size(self, x):
        return -self.parents[self.root(x)]
    
######################################################

N,M,K=mint()
T=UnionFind(N)
block=[0]*N
for _ in range(M):
    a,b=mint()
    T.union(a-1,b-1)
    block[a-1]+=1
    block[b-1]+=1
for _ in range(K):
    c,d=mint()
    if T.same(c-1,d-1):
        block[c-1]+=1
        block[d-1]+=1
ans=[T.size(i)-block[i]-1 for i in range(N)]
lprint(ans,' ')