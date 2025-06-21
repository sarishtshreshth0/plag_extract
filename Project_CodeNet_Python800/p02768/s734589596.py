mod=10**9+7
import math
import sys
from collections import deque
import heapq
import copy
import itertools
from itertools import permutations
from itertools import combinations
import bisect
def mi() : return map(int,sys.stdin.readline().split())
def ii() : return int(sys.stdin.readline().rstrip())
def i() : return sys.stdin.readline().rstrip()
n,a,b=mi()
c=pow(2,n,mod)-1
fact=[1]*(2*10**5+1)
for i in range(1,2*10**5+1):
  fact[i]=(fact[i-1]*i)%mod
def nCk(n,k):
  h=1
  for i in range(k):
    h=(h*(n-i))%mod
  x=h*pow(fact[k],mod-2,mod)
  return(x)
print((c-nCk(n,a)-nCk(n,b))%mod)