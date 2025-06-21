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

n = inn()
a = inl()
h = {0:1}
acc = 0
for x in a:
    acc += x
    if acc not in h:
        h[acc] = 0
    h[acc] += 1
sm = 0
for x in h:
    sm += h[x]*(h[x]-1)//2
print(sm)
