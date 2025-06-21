import sys, bisect, math, itertools, string, queue, copy
import numpy as np
import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

n,a,b = inpm()

ret = (pow(2,n,mod) - 1)

modinv_table = [-1] * (max(a,b)+1)
modinv_table[1] = 1
for i in range(2, max(a,b)+1):
    modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod

def comb(n,r):
    x = 1
    y = 1
    for i in range(r):
        x = x*(n-i)%mod #コンビネーションの分子
        y = y*(i+1)%mod #コンビネーションの分母
    return (x * pow(y, mod-2, mod) % mod)
aa = comb(n,a)
bb = comb(n,b)

ret = (ret - aa - bb) % mod

print(ret)