import sys
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from math import *

sys.setrecursionlimit(10**6)
INF = 10**20

def mint():
    return map(int,input().split())
def lint():
    return map(int,input().split())
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])

N,A = int(input()),lint()
S = [0]*(10**5+10)
for a in A:
    S[a-1] += 1
    S[a] += 1
    S[a+1] += 1
print(max(S))