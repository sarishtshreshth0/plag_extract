#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

import math
def dig(n):
    for i in range(1,12):
        if n<10**i:
            return i

n = inn()
mn = BIG
en = int(math.sqrt(n))+2
for i in range(1,en):
    if n%i==0:
        mn = min(mn,dig(n//i))
print(mn)
