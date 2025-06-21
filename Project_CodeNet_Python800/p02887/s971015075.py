ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq

n = ni()
s = input()
cnt = 0
prev=""
for i in range(n):
    if prev==s[i]:
        pass
    else:
        cnt+=1
    prev=s[i]
print(cnt)
