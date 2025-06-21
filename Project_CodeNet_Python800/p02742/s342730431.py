import sys
import math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
H,W= LI()

if H == 1 or W == 1:
    print(1)
else:
    ans = (H*W+1)/2
    print(int(ans))