#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
#たね：gcdは交換法則がなりたち、どこからでも計算していい
#だけど、逆演算ができない 
#(gcd(x,4)==2　を満たすxは2以上の偶数ならなんでもよく
#つまり一つに定まらない）
#そのかわり、"最後の一個以外"を計算してしまうことはできる

#初見殺しじゃねーか
from fractions import gcd
def resolve():
    N,=pin()
    A=tupin()
    lgcd,rgcd=[0]*(N),[0]*(N)
    ltemp,tempr=A[0],A[-1]
    for g in range(N):
        ltemp=gcd(ltemp,A[g])
        lgcd[g]=ltemp
        #print(tempr,A[N-g-1])
        tempr=gcd(tempr,A[N-g-1])
        
        rgcd[N-g-1]=tempr
    #print(lgcd,A,rgcd)
    ans=1
    for i in range((N)):
        a,t=0,0
        if i==0:
            t=rgcd[1]
        elif i==N-1:
            t=lgcd[N-2]
        else:
            t=gcd(lgcd[i-1],rgcd[i+1])
        ans=max(ans,t)
    print(ans)
#%%submit!
resolve()