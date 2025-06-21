import sys
import time
#from collections import deque, Counter, defaultdict
#from fractions import gcd
#import bisect
#import heapq
import math
start=time.time()
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))
a,b = rl()
c=a%4
d=b%4
ans=0
for i in range(4-c):
    ans^=a+i
for i in range(d+1):
    ans^=b-i
print(ans)