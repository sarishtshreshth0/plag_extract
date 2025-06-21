# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

q,h,s,d=map(int,input().split())
n=int(input())
s=min(q*4,h*2,s)
if s*2<d:
    print(s*n)
else:
    if n%2:
        print(d*(n//2)+s)
    else:
        print(d*(n//2))