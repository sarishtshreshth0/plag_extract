#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
from collections import Counter
def resolve():
    Q,H,S,D=pin()
    N=int(input())
    Q*=4
    H*=2
    s=min(Q,H,S)
    t=N%2
    ans=0
    if s*2>D:
        ans+=D*(N//2)
        #print(ans)
        N=t
    ans+=N*s
    print(ans)
#%%submit!
resolve()