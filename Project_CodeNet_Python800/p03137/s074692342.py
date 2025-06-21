import bisect,collections,copy,heapq,itertools,math,string
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n, m = MAP()
x = sorted(LIST())
dx = [x[i+1]-x[i] for i in range(m-1)]
dx.sort(reverse=True)

if n >= m:
    print(0)
else:
    print(x[m-1]-x[0]-sum(dx[0:n-1]))