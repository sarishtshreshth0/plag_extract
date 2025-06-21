import sys
from collections import deque
import numpy as np
import math
sys.setrecursionlimit(10**6)
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def solve():
    if w==1 or h==1:
        print(1)
        return
    ans = 0
    ans += math.ceil(w/2)*math.ceil(h/2)
    ans += (w//2)*(h//2)
    print(ans)
    return

if __name__=='__main__':
    h,w = IL()
    solve()