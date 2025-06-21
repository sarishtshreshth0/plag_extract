import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
a, b = M()
if a == 1:
    a += 13
if b == 1:
    b += 13
if a == b:
    print('Draw')
elif a < b:
    print('Bob')
else:
    print('Alice')