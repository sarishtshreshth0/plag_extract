import math
import collections
import sys

#input = sys.stdin.readline
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]

a,b=MI()
if a==2 or b==2:
    print("No")
else:
    print("Yes")