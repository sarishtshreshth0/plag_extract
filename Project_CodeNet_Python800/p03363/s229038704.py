ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
co = collections.Counter()
n = ni()
A = lma()
s = 0
co[0]+=1
for a in A:
    s+=a
    co[s]+=1

ans = 0
for val in co.values():
    ans+= val*(val-1)//2
print(ans)
