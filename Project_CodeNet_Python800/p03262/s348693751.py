import bisect,collections,copy,heapq,itertools,math,string
import sys
def li(): return map(int,sys.stdin.readline().rstrip().split())
def lf(): return map(float,sys.stdin.readline().rstrip().split())
def ls(): return sys.stdin.readline().rstrip().split()

n, x = li()
p = list(li())
gcd = abs(x-p[0])
for i in range(n):
    gcd = math.gcd(gcd, abs(x-p[i]))

print(gcd)    